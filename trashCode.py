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

# Example of using the optimization function
source_code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.[-+++------][+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.]++-"
optimized_code = optimize_successive_loops(source_code)

# Print the optimized code for review
print(optimized_code)
