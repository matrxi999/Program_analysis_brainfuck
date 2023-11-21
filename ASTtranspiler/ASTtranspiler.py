from ASTgenerator import ast
detected = False

def delete_first_unexecutable_loop(ast):
    """If program starts with loop or the first loop is not 
    preceeded by '+', '-' or ',' then it will not be executed.
    Therefore can be deleted"""

    for node in ast.children:
        if node.kind == "command" and node.value in ['+', '-', ',']:
            return
        if node.kind == "loop_start":
            ast.children.remove(node)
            return delete_first_unexecutable_loop(ast)
        
def remove_redundant_sequences_before_input(ast):
    """Any "+" and "-" directly before input (",") will be deleted 
    since it would be overwritten anyway"""

    i = 0
    while i < len(ast.children):
        if ast.children[i].kind == "command" and ast.children[i].value == ',':
            j = i - 1
            while j >= 0 and ast.children[j].kind == "command" and ast.children[j].value in ['+', '-']:
                del ast.children[j]
                j -= 1
                i -= 1
        i += 1




def translate_from_ast(ast, optimize_arithmetic=False, optimize_pointer=False, optimize_clear_loops=False, optimize_consecutive_loops=False, delete_first_loop=False, remove_redundant_sequences=False, copy_loop_optimization=False):
    if delete_first_loop:
        delete_first_unexecutable_loop(ast)

    if remove_redundant_sequences:
        remove_redundant_sequences_before_input(ast)

    out = [
        "import time",
        "start = time.time()",
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
        """Handle "+" and "-" that cancle out and then compress sequences of "+" and "-" into single command like "+++" -> add(3)"""
        count = 0
        current_index = index
        while current_index < len(parent.children) and parent.children[current_index].value in ['+', '-']:
            count += 1 if parent.children[current_index].value == '+' else -1
            current_index += 1

        if count > 0:
            return indent + f"add({count})", current_index
        elif count < 0:
            return indent + f"subtract({-count})", current_index
        return None, current_index


    def optimize_pointer_commands(node, parent, index, indent):
        """Same as above but for "<" and ">" """
        count = 0
        current_index = index
        while current_index < len(parent.children) and parent.children[current_index].value in ['<', '>']:
            count += 1 if parent.children[current_index].value == '>' else -1
            current_index += 1

        if count > 0:
            return indent + f"index += {count}", current_index
        elif count < 0:
            return indent + f"index -= {-count}", current_index
        return None, current_index

    def detect_special_loop(node, index):
        """
        Detects loops with the pattern [->+>+<<] (which basically copy the content of first cell into X number of next cells) and generates the transpiled output.

        Args:
        - node: The loop node to check.
        - index: The current data pointer index.

        Returns:
        - A tuple (detected, new_index, transpiled_code) where:
            'detected' is a boolean indicating if the pattern was detected.
            'new_index' is the index at which the loop ends.
            'transpiled_code' is the list of strings representing the Python code if detected.
        - (False, index, None) otherwise.
        """

        children = node.children
        # The first command should be a single '-'
        if not (len(children) > 2 and children[0].kind == "command" and children[0].value == '-'):
            return False, index, None
        
        steps = 0
        # Loop through the commands looking for '>+' pairs
        for i in range(1, len(children) - 1, 2):
            if (children[i].kind == "command" and children[i].value == '>' and
                    children[i + 1].kind == "command" and children[i + 1].value == '+'):
                steps += 1
            else:
                break  # Stop if any other pattern is found

        # Check if the number of '<' commands equals the number of steps ">+"
        if all(child.kind == "command" and child.value == '<' for child in children[-steps:-1]) and len(children) == (1+steps*2+steps+1):
            # generate transpiled code
            transpiled_code = [
                f"temp = data[index]",
                f"data[index] = 0"
            ]
            new_index = index
            for _ in range(steps):
                new_index += 1
                transpiled_code.append(f"data[index + {_+1}] = temp")
            new_index -= steps  # Move the index back to the original position

            return True, new_index, transpiled_code

        return False, index, None



    def optimize_clear_loop(node, indent):
        """ Look for [-] pattern which is called "clear loop" because it just zeroes out the current cell 
        and when found replace it with single command assigning 0 to memory cell"""

        if node.kind == "loop_start" and len(node.children) == 2:
            child = node.children[0]
            if child.kind == "command" and child.value == '-':
                return indent + "data[index] = 0"
        return None


    def optimize_consecutive_loop(node, parent, index):
        """Remove loops that are placed directly after a loop. They will not get executed anyway 
        since on the exit of the first loop we must have current cell value equal 0."""

        if node.kind == "loop_start":
            current_index = index + 1
            while current_index < len(parent.children) and parent.children[current_index].kind == "loop_start":
                current_index += 1
            return current_index - 1
        return index + 1

    def translate_node(node, parent, index, indent_level=0, optimize_clear_loops=False, optimize_consecutive_loops=False, copy_loop_optimization=False):
        indent = "    " * indent_level
        global detected
        if node.kind == "command" and not detected:
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
            if copy_loop_optimization:
                detected, new_index, transpiled_code = detect_special_loop(node, index)
            if detected and copy_loop_optimization:
                out.extend([indent + line for line in transpiled_code])
                
                index = new_index
            
            if optimize_consecutive_loops:
                index = optimize_consecutive_loop(node, parent, index)

            if optimize_clear_loops:
                clear_loop_translation = optimize_clear_loop(node, indent)
                if clear_loop_translation:
                    out.append(clear_loop_translation)
                    return index + 1  # Skip the clear loop

            if not detected: out.append(indent + "while data[index] != 0:")
            child_index = 0
            while child_index < len(node.children):
                child_index = translate_node(node.children[child_index], node, child_index, indent_level + 1, optimize_clear_loops, optimize_consecutive_loops)
            return index + 1
        elif node.kind == "loop_end":
            if not detected: out.append(indent + "# End of loop")
            detected = False
            return index + 1
        else:
            return index+1
    
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
        child_index = translate_node(ast.children[child_index], ast, child_index, 0, optimize_clear_loops, optimize_consecutive_loops,copy_loop_optimization)

    return '\n'.join(out) + '\n' + "end = time.time()" + '\n' + "print(end - start)"


optimized_python_code = translate_from_ast(ast, optimize_arithmetic=False, optimize_pointer=False, optimize_consecutive_loops=False, optimize_clear_loops=False, delete_first_loop=False, remove_redundant_sequences=False, copy_loop_optimization=True)

# Write the optimized Python code to a file
with open("Program_analysis_brainfuck\ASTtranspiler/OptimizedOutput.py", "w", encoding="utf-8") as text_file:
    text_file.write(optimized_python_code)