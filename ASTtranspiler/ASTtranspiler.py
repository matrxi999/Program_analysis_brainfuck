from ASTgenerator import ast

def translate_from_ast(ast, optimize_consecutive_operations=False):
    out = [
        "data = [0]*30000",
        "index = 0",
        "def bf_add(x):",
        "    global index",
        "    data[index] = (data[index] + x) % 256",
        "def bf_sub(x):",
        "    global index",
        "    data[index] = (data[index] - x) % 256",
        "def bf_output():",
        "    global index",
        "    print(chr(data[index]), end='')",
        "def bf_input():",
        "    global index",
        "    data[index] = ord(input())",
    ]

    def get_next_sibling(node, parent):
        if parent and node in parent.children:
            current_index = parent.children.index(node)
            if current_index + 1 < len(parent.children):
                return parent.children[current_index + 1]
        return None

    def translate_node(node, parent, indent_level=0):
        indent = "    " * indent_level
        if node.kind == "command":
            return translate_command(node, parent, indent)
        elif node.kind == "loop_start":
            out.append(indent + "while data[index] != 0:")
            for child in node.children:
                translate_node(child, node, indent_level + 1)
        elif node.kind == "loop_end":
            out.append(indent + "# End of loop")

    def translate_command(node, parent, indent):
        command = node.value
        if command in ['+', '-'] and optimize_consecutive_operations:
            count = 0
            while node and node.kind == "command" and node.value in ['+', '-']:
                count = count + 1 if node.value == '+' else count - 1
                node = get_next_sibling(node, parent)
            if count > 0:
                out.append(indent + f"bf_add({count})")
            elif count < 0:
                out.append(indent + f"bf_sub({-count})")
            return node  # Return the next node to process
        else:
            return default_translate(command, indent)

    def default_translate(command, indent):
        if command == '>':
            out.append(indent + "index += 1")
        elif command == '<':
            out.append(indent + "index -= 1")
        elif command == '.':
            out.append(indent + "bf_output()")
        elif command == ',':
            out.append(indent + "bf_input()")

    for node in ast.children:
        current_node = node
        while current_node:
            current_node = translate_node(current_node, ast)

    return '\n'.join(out)


optimized_python_code = translate_from_ast(ast, optimize_consecutive_operations=False)

# Write the optimized Python code to a file
with open("ASTtranspiler/OptimizedOutput.py", "w", encoding="utf-8") as text_file:
    text_file.write(optimized_python_code)
