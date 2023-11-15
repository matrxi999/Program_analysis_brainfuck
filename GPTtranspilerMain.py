def optimize_clear_loop(sourcecode):
    """Optimize clear loop [-] in Brainfuck code."""
    return sourcecode.replace('[-]', '0')  # Replace with '0' as a marker for clearing the cell

def optimize_successive_loops(sourcecode):
    """Optimize successive loops in Brainfuck code."""
    optimized_code = ""
    i = 0

    while i < len(sourcecode):
        # Check for successive loops pattern
        if sourcecode[i] == ']' and i + 1 < len(sourcecode) and sourcecode[i + 1] == '[':
            # Skip the next loop
            optimized_code += sourcecode[i]
            i += 2
            loop_lvl = 1
            while i < len(sourcecode) and loop_lvl > 0:
                if sourcecode[i] == '[':
                    loop_lvl += 1
                elif sourcecode[i] == ']':
                    loop_lvl -= 1
                i += 1
        else:
            optimized_code += sourcecode[i]
            i += 1
    return optimized_code

def optimize_not_executing_loop(sourcecode):
    # New optimization to remove loops following clear loop if conditions are met
    if not any(c in sourcecode.split('[')[0] for c in ['+','-',',']):
        # Find the matching closing bracket for the loop
        loop_depth = 1
        idx = sourcecode.find("[")
        for i, char in enumerate(sourcecode[idx+1:], start=idx+1):
            if char == '[':
                loop_depth += 1
            elif char == ']':
                loop_depth -= 1
                if loop_depth == 0:
                    # Remove the loop from the code
                    return optimize_not_executing_loop(sourcecode[:idx] + sourcecode[i+1:])
        # If loop not properly closed, return the optimized code as is
        return sourcecode
    else:
        return sourcecode

def optimize_increments_before_input(sourcecode):
    """Remove all '+' and '-' sequences directly before ',' as they are redundant."""
    optimized_code = ""
    i = 0

    while i < len(sourcecode):
        if sourcecode[i] == ',':
            # Remove any '+' or '-' characters immediately before ','
            j = i
            while j > 0 and sourcecode[j - 1] in '+-':
                j -= 1
            optimized_code += sourcecode[:j] + ','
            sourcecode = sourcecode[i + 1:]
            i = 0
        else:
            i += 1

    # Append any remaining part of the source code
    optimized_code += sourcecode
    return optimized_code

def optimize_increments(sourcecode):
    """Combine consecutive + and - operations."""
    new_code = []
    count = 0

    for char in sourcecode:
        if char in ['+', '-']:
            count = count + 1 if char == '+' else count - 1
        else:
            if count:
                new_code.append(('+'*abs(count) if count > 0 else '-'*abs(count)))
                count = 0
            new_code.append(char)

    if count:  # Append any remaining counts
        new_code.append(('+'*abs(count) if count > 0 else '-'*abs(count)))
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
                new_code.append(('>'*abs(count) if count > 0 else '<'*abs(count)))
                count = 0
            new_code.append(char)

    if count:  # Append any remaining counts
        new_code.append(('>'*abs(count) if count > 0 else '<'*abs(count)))
    return ''.join(new_code)

def translate(sourcecode, optimize_increment=False, optimize_pointer=False, optimize_not_executing_loops=False, successive_loops=False, clear_loop_optimization=False, optimize_before_input=False):
    if optimize_before_input:
        sourcecode = optimize_increments_before_input(sourcecode)
    if optimize_increment:
        sourcecode = optimize_increments(sourcecode)  # Function definition needed
    if optimize_pointer:
        sourcecode = optimize_pointers(sourcecode)  # Function definition needed
    if optimize_not_executing_loops:
        sourcecode = optimize_not_executing_loop(sourcecode)  # Function definition needed
    if successive_loops:
        sourcecode = optimize_successive_loops(sourcecode)  # Function definition needed
    if clear_loop_optimization:
        sourcecode = optimize_clear_loop(sourcecode)
    
    out = [
        "data = [0]*30000",
        "index = 0",
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
        "    print(chr(data[index]), end='')",
        "def bf_input():",
        "    global index",
        "    data[index] = ord(input())",
        "def zero_cell():",
        "    global index",
        "    data[index] = 0",
    ]

    indent_level = 0
    i = 0
    while i < len(sourcecode):
        s = sourcecode[i]
        indent = "    " * indent_level

        if s == '>':
            move = 1
            while i + 1 < len(sourcecode) and sourcecode[i + 1] == '>' and optimize_pointer:
                i += 1
                move += 1
            out.append(indent + f"index += {move}")
        elif s == '<':
            move = 1
            while i + 1 < len(sourcecode) and sourcecode[i + 1] == '<' and optimize_pointer:
                i += 1
                move += 1
            out.append(indent + f"index -= {move}")
        elif s == '+':
            add = 1
            while i + 1 < len(sourcecode) and sourcecode[i + 1] == '+' and optimize_increment:
                i += 1
                add += 1
            out.append(indent + f"bf_add({add})")
        elif s == '-':
            sub = 1
            while i + 1 < len(sourcecode) and sourcecode[i + 1] == '-' and optimize_increment:
                i += 1
                sub += 1
            out.append(indent + f"bf_sub({sub})")
        elif s == "0":
            out.append(indent + "zero_cell()")
        elif s == '.':
            out.append(indent + "bf_output()")
        elif s == ',':
            out.append(indent + "bf_input()")
        elif s == '[':
            out.append(indent + "while data[index] != 0:")
            indent_level += 1
        elif s == ']':
            indent_level -= 1
            indent = "    " * indent_level
            out.append(indent + "# End of loop")
        i += 1

    return '\n'.join(out)

# Example usage with optimizations enabled
with open("brainfucktest.b", 'r') as file:
    sourcecode = file.read()

optimized_python_code = translate(sourcecode,optimize_increment=True, optimize_pointer=True, optimize_not_executing_loops=True, successive_loops=True, clear_loop_optimization=True, optimize_before_input=True)

# Write the optimized Python code to a file
with open("OptimizedOutput.py", "w", encoding="utf-8") as text_file:
    text_file.write(optimized_python_code)
