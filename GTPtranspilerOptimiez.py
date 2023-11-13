def optimize_increments(sourcecode):
    """Combine consecutive + and - operations."""
    new_code = []
    count = 0

    for char in sourcecode:
        if char in ['+', '-']:
            count = count + 1 if char == '+' else count - 1
        else:
            if count:
                new_code.append(('+' if count > 0 else '-') + str(abs(count)))
                count = 0
            new_code.append(char)

    if count:  # Append any remaining counts
        new_code.append(('+' if count > 0 else '-') + str(abs(count)))

    return ''.join(new_code)

def optimize_pointers(sourcecode):
    """Combine consecutive < and > operations."""
    new_code = []
    count = 0

    for char in sourcecode:
        if char in ['<', '>']:
            count = count + 1 if char == '>' else count - 1
        else:
            if count:
                new_code.append(('>' if count > 0 else '<') + str(abs(count)))
                count = 0
            new_code.append(char)

    if count:  # Append any remaining counts
        new_code.append(('>' if count > 0 else '<') + str(abs(count)))

    return ''.join(new_code)

def translate(sourcecode, optimize_increment=False, optimize_pointer=False, set_zero_optimization=False):
    if optimize_increment:
        sourcecode = optimize_increments(sourcecode)
    if optimize_pointer:
        sourcecode = optimize_pointers(sourcecode)
    
    out = [
        "data = [0]*30000",
        "index = 0",
        "output = ''",
        "def bf_add(x):",
        "    global index",
        "    data[index] = (data[index] + x) % 256",
        "def bf_sub(x):",
        "    global index",
        "    data[index] = (data[index] - x) % 256",
        "def bf_clear():",
        "    global index",
        "    data[index] = 0",
        "def bf_output():",
        "    global index",
        "    output += chr(data[index])",
        "def bf_input():",
        "    global index",
        "    data[index] = ord(input())",
        "",
    ]

    # Parsing and Translating the Brainfuck code
    i = 0
    while i < len(sourcecode):
        s = sourcecode[i]
        if s == '>':
            move = 1
            while i + 1 < len(sourcecode) and sourcecode[i + 1] == '>':
                i += 1
                move += 1
            out.append(f"index += {move}")
        elif s == '<':
            move = 1
            while i + 1 < len(sourcecode) and sourcecode[i + 1] == '<':
                i += 1
                move += 1
            out.append(f"index -= {move}")
        elif s == '+':
            add = 1
            while i + 1 < len(sourcecode) and sourcecode[i + 1] == '+':
                i += 1
                add += 1
            out.append(f"bf_add({add})")
        elif s == '-':
            sub = 1
            while i + 1 < len(sourcecode) and sourcecode[i + 1] == '-':
                i += 1
                sub += 1
            out.append(f"bf_sub({sub})")
        elif s == '.':
            out.append("bf_output()")
        elif s == ',':
            if not (i > 0 and sourcecode[i - 1] in '+-'):
                # Only reset the cell if the previous command wasn't + or -
                out.append("bf_input()")
        elif s == '[':
            # Special optimization for clear loop
            if set_zero_optimization and i + 2 < len(sourcecode) and sourcecode[i+1] == '-' and sourcecode[i+2] == ']':
                out.append("bf_clear()")
                i += 2  # Skip past the clear loop pattern
            else:
                out.append("while data[index] != 0:")
        elif s == ']':
            out.append("# End of loop")
        i += 1

    # Joining the code with new lines and returning
    return '\n'.join(out)

# Example usage with optimizations enabled
optimized_python_code = translate(">++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++."
                                  "------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.",
                                  optimize_increment=True, optimize_pointer=True, set_zero_optimization=True)

# Write the optimized Python code to a file
with open("OptimizedOutput.py", "w", encoding="utf-8") as text_file:
    text_file.write(optimized_python_code)
