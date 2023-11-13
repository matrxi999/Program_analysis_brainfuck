# Brainfuck to Python Transpiler
def translate(sourcecode):
    # Initial setup for Python output
    python_output = [
        "tape = [0] * 30000",  # Initialize tape with 30,000 cells
        "ptr = 0",             # Pointer to current cell
        "def bf_add(x): global ptr; tape[ptr] = (tape[ptr] + x) % 256",  # Add function
        "def bf_sub(x): global ptr; tape[ptr] = (tape[ptr] - x) % 256",  # Subtract function
        "def bf_output(): print(chr(tape[ptr]), end='')",                # Output function
        "def bf_input(): global ptr; tape[ptr] = ord(input('Input a character: ')[0])",  # Input function
    ]

    # Convert Brainfuck commands to Python functions
    cmd_to_function = {
        '+': 'bf_add(1)',
        '-': 'bf_sub(1)',
        '>': 'ptr += 1',
        '<': 'ptr -= 1',
        '.': 'bf_output()',
        ',': 'bf_input()',
    }

    # Process source code and handle loops
    open_loops = 0
    for command in sourcecode:
        if command in cmd_to_function:
            python_output.append("    " * open_loops + cmd_to_function[command])  # Apply current indentation
        elif command == '[':
            python_output.append("    " * open_loops + "while tape[ptr] != 0:")  # Open a loop
            open_loops += 1
        elif command == ']':
            if open_loops == 0:  # Check for unbalanced loops
                raise ValueError("Unbalanced loop detected: too many closing brackets")
            open_loops -= 1  # Close a loop

    if open_loops > 0:  # Check if all loops are closed
        raise ValueError("Unbalanced loop detected: missing closing brackets")

    # Return the translated code
    return '\n'.join(python_output)

# Transpile Brainfuck code to Python
bf_program = ">++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+."
python_code = translate(bf_program)

# Write the Python code to a file
with open("TranslatedOutput.py", "w", encoding="utf-8") as text_file:
    text_file.write(python_code)
