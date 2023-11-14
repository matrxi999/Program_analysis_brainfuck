def optimize_clear_loop(sourcecode):
    """Optimize clear loop [-] in Brainfuck code."""
    return sourcecode.replace('[-]', '0')  # Replace with '0' as a marker for clearing the cell

def optimize_loops_after_clear_loop(sourcecode):
    """Remove loops that immediately follow a [-] clear loop."""
    i = 0
    optimized_code = ""
    while i < len(sourcecode):
        if sourcecode[i:i+3] == '[-]':
            optimized_code += '[-]'  # Mark the clear loop
            i += 3
            # Skip the loop that follows the clear loop
            if i < len(sourcecode) and sourcecode[i] == '[':
                loop_depth = 1
                i += 1
                while i < len(sourcecode) and loop_depth > 0:
                    if sourcecode[i] == '[':
                        loop_depth += 1
                    elif sourcecode[i] == ']':
                        loop_depth -= 1
                    i += 1
        else:
            optimized_code += sourcecode[i]
            i += 1

    return optimized_code

def optimize_not_executing_loop(sourcecode):
    # New optimization to remove loops following clear loop if conditions are met
    if sourcecode.startswith('[') and not any(c in sourcecode.split('[')[0] for c in ['+',',']):
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

def translate(sourcecode, optimize_increment=False, optimize_pointer=False, optimize_not_executing_loops=False, loops_after_clear_loops=False, clear_loop_optimization=False, optimize_before_input=False):
    if optimize_before_input:
        sourcecode = optimize_increments_before_input(sourcecode)
    if optimize_increment:
        sourcecode = optimize_increments(sourcecode)
    if optimize_pointer:
        sourcecode = optimize_pointers(sourcecode)
    if optimize_not_executing_loops:
        sourcecode = optimize_not_executing_loop(sourcecode)
    if loops_after_clear_loops:
        sourcecode = optimize_loops_after_clear_loop(sourcecode)
    if clear_loop_optimization:
        sourcecode = optimize_clear_loop(sourcecode)
    
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
        "def zero_cell():",
        "    global index",
        "    data[index] = 0",
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
        elif s == "0":
            out.append("zero_cell()")
        elif s == '.':
            out.append("bf_output()")
        elif s == ',':
            out.append("bf_input()")
        elif s == '[':
            out.append("while data[index] != 0:")
        elif s == ']':
            out.append("# End of loop")
        i += 1

    # Joining the code with new lines and returning
    return '\n'.join(out)

# Example usage with optimizations enabled
optimized_python_code = translate(">++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++."
                                  "------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.",
                                  optimize_increment=False, optimize_pointer=False, optimize_not_executing_loops=False, loops_after_clear_loops=False, clear_loop_optimization=False, optimize_before_input=False)

# Write the optimized Python code to a file
with open("OptimizedOutput.py", "w", encoding="utf-8") as text_file:
    text_file.write(optimized_python_code)
