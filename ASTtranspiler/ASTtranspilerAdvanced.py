from ASTgenerator import ast

def delete_first_unexecutable_loop(ast):
    for node in ast.children:
        if node.kind == "command" and node.value in ['+', '-', ',']:
            # Found a modifying command before any loop, no optimization possible
            return
        if node.kind == "loop_start":
            # Found a loop that hasn't been preceded by a modifying command, remove it
            ast.children.remove(node)
            return delete_first_unexecutable_loop(ast)
        
def remove_redundant_sequences_before_input(ast):
    i = 0
    while i < len(ast.children):
        if ast.children[i].kind == "command" and ast.children[i].value == ',':
            # Find and remove all preceding '+' and '-' commands
            j = i - 1
            while j >= 0 and ast.children[j].kind == "command" and ast.children[j].value in ['+', '-']:
                del ast.children[j]
                j -= 1
                i -= 1  # Adjust the index since we're removing elements
        i += 1


def translate_from_ast(ast, optimize_arithmetic=False, optimize_pointer=False, optimize_clear_loops=False, optimize_consecutive_loops=False, delete_first_loop=False, remove_redundant_sequences=False):
    if delete_first_loop:
        delete_first_unexecutable_loop(ast)

    if remove_redundant_sequences:
        remove_redundant_sequences_before_input(ast)

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

    def optimize_arithmetic_commands(node, parent, index, indent):
        count = 0
        current_index = index
        while current_index < len(parent.children) and parent.children[current_index].value == node.value:
            count += 1 if node.value == '+' else -1
            current_index += 1
        if count > 0:
            return indent + f"add({count})", current_index
        elif count < 0:
            return indent + f"subtract({-count})", current_index

    def optimize_pointer_commands(node, parent, index, indent):
        count = 0
        current_index = index
        while current_index < len(parent.children) and parent.children[current_index].value == node.value:
            count += 1 if node.value == '>' else -1
            current_index += 1
        if count > 0:
            return indent + f"index += {count}", current_index
        elif count < 0:
            return indent + f"index -= {-count}", current_index

    def optimize_clear_loop(node, indent):
        # Check if the node represents a '[-]' pattern
        if node.kind == "loop_start" and len(node.children) == 2:
            child = node.children[0]
            if child.kind == "command" and child.value == '-':
                return indent + "data[index] = 0"
        return None


    def optimize_consecutive_loop(node, parent, index):
        if node.kind == "loop_start":
            current_index = index + 1
            while current_index < len(parent.children) and parent.children[current_index].kind == "loop_start":
                current_index += 1
            return current_index - 1
        return index + 1

    def translate_node(node, parent, index, indent_level=0, optimize_clear_loops=False, optimize_consecutive_loops=False):
        indent = "    " * indent_level
        if node.kind == "command":
            if node.kind == "command":
                if optimize_arithmetic and node.value in ['+', '-']:
                    command_translation, next_index = optimize_arithmetic_commands(node, parent, index, indent)
                elif optimize_pointer and node.value in ['<', '>']:
                    command_translation, next_index = optimize_pointer_commands(node, parent, index, indent)
                else:
                    command_translation = translate_command(node, indent)
                    next_index = index + 1
                if command_translation:
                    out.append(command_translation)
                return next_index
        elif node.kind == "loop_start":
            # Apply consecutive loop optimization
            if optimize_consecutive_loops:
                index = optimize_consecutive_loop(node, parent, index)

            # Apply clear loop optimization
            if optimize_clear_loops:
                clear_loop_translation = optimize_clear_loop(node, indent)
                if clear_loop_translation:
                    out.append(clear_loop_translation)
                    return index + 1  # Skip the clear loop

            out.append(indent + "while data[index] != 0:")
            child_index = 0
            while child_index < len(node.children):
                child_index = translate_node(node.children[child_index], node, child_index, indent_level + 1, optimize_clear_loops, optimize_consecutive_loops)
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

    child_index = 0
    while child_index < len(ast.children):
        child_index = translate_node(ast.children[child_index], ast, child_index, 0, optimize_clear_loops, optimize_consecutive_loops)

    return '\n'.join(out)


optimized_python_code = translate_from_ast(ast, optimize_arithmetic=True, optimize_pointer=True, optimize_consecutive_loops=True, optimize_clear_loops=True, delete_first_loop=True, remove_redundant_sequences=True)

# Write the optimized Python code to a file
with open("ASTtranspiler/OptimizedOutput.py", "w", encoding="utf-8") as text_file:
    text_file.write(optimized_python_code)