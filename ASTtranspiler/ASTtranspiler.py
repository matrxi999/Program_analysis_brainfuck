from ASTgenerator import ast


def translate_from_ast(ast, optimize_consecutive_operations=False):
    out = [
        "data = [0]*30000",
        "index = 0",
        "def add(x):",
        "    global index",
        "    data[index] = (data[index] + x) % 256",
        "def subtract(x):",
        "    global index",
        "    data[index] = (data[index] - x) % 256",
        "def output():",
        "    global index",
        "    print(chr(data[index]), end='')",
        "def input_():",
        "    global index",
        "    data[index] = ord(input())",
    ]

    def translate_node(node, parent, index, indent_level=0):
        indent = "    " * indent_level
        if node.kind == "command":
            if optimize_consecutive_operations:
                command_translation, next_index = translate_optimized_command(node, parent, index, indent)
            else:
                command_translation = translate_command(node, indent)
                next_index = index + 1
            if command_translation:
                out.append(command_translation)
            return next_index
        elif node.kind == "loop_start":
            out.append(indent + "while data[index] != 0:")
            child_index = 0
            while child_index < len(node.children):
                child_index = translate_node(node.children[child_index], node, child_index, indent_level + 1)
            return index + 1
        elif node.kind == "loop_end":
            out.append(indent + "# End of loop")
            return index + 1

    def translate_command(node, indent):
        command_translations = {
            '>': "index += 1",
            '<': "index -= 1",
            '+': "add(1)",
            '-': "subtract(1)",
            '.': "output()",
            ',': "input_()"
        }
        return indent + command_translations.get(node.value, "")

    def translate_optimized_command(node, parent, index, indent):
        command = node.value
        if command in ['+', '-', '<', '>'] and optimize_consecutive_operations:
            count = 0
            current_index = index
            while current_index < len(parent.children) and parent.children[current_index].value == command:
                if command in ['+', '>']:
                    count += 1
                else:  # '-', '<'
                    count -= 1
                current_index += 1

            if command in ['+', '-']:
                if count > 0:
                    return indent + f"add({count})", current_index
                elif count < 0:
                    return indent + f"subtract({-count})", current_index
            elif command in ['<', '>']:
                if count > 0:
                    return indent + f"index += {count}", current_index
                elif count < 0:
                    return indent + f"index -= {-count}", current_index
        else:
            return translate_command(node, indent), index + 1

    child_index = 0
    while child_index < len(ast.children):
        child_index = translate_node(ast.children[child_index], ast, child_index)

    return '\n'.join(out)

optimized_python_code = translate_from_ast(ast, optimize_consecutive_operations=True)

# Write the optimized Python code to a file
with open("ASTtranspiler/OptimizedOutput.py", "w", encoding="utf-8") as text_file:
    text_file.write(optimized_python_code)
