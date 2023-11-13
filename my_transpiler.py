def optimize(sourcecode):
    optimized_code = []
    program_position = 0
    while program_position < len(sourcecode):
        command = sourcecode[program_position]
        count = 1

        # Handle repetitive characters
        while program_position + count < len(sourcecode) and sourcecode[program_position + count] == command:
            count += 1

        if command == "+":
            optimized_code.append(("add", count))
        elif command == "-":
            optimized_code.append(("sub", count))
        elif command == ">":
            optimized_code.append(("right", count))
        elif command == "<":
            optimized_code.append(("left", count))
        elif command == ".":
            optimized_code.append(("putch",count))
        elif command == ",":
            optimized_code.append(("getch",count))
        elif command == "[":
            loop_end = find_loop_end(sourcecode, program_position)
            loop_body = sourcecode[program_position + 1:loop_end]
            if len(loop_body) == 1 and loop_body[0] == "-":
                optimized_code.append(("clear",))
            else:
                optimized_code.append(("loop", optimize(loop_body)))
            program_position = loop_end
        program_position += 1

    return optimized_code


def find_loop_end(sourcecode, start):
    level = 0
    i = start
    while i < len(sourcecode):
        if sourcecode[i] == "[":
            level += 1
        elif sourcecode[i] == "]":
            level -= 1
            if level == 0:
                return i
        i += 1

    raise ValueError("Unmatched '[' in Brainfuck code")


def translate_optimized(optimized_code):
    out = [
        (0, "from collections import defaultdict"),
        (0, "from msvcrt import getch"),
        (0, "putch = lambda x: print(chr(x), end='')"),
        (0, "data = defaultdict(int)"),
        (0, "index = 0"),
        (0, "def add(x):data[index] = (data[index] + x) % 256"),
        (0, "def sub(x):data[index] = (data[index] - x) % 256"),
    ]

    for item in optimized_code:
        if item[0] == "add":
            out.append((0, f"add({item[1]!r})"))
        elif item[0] == "sub":
            out.append((0, f"sub({item[1]!r})"))
        elif item[0] == "right":
            out.append((0, f"index += {item[1]!r}"))
        elif item[0] == "left":
            out.append((0, f"index -= {item[1]!r}"))
        elif item[0] == "putch":
            out.append((0, "putch(data[index])"))
        elif item[0] == "getch":
            out.append((0, "data[index] = getch()[0]"))
        elif item[0] == "clear":
            out.append((0, "data[index] = 0"))
        elif item[0] == "loop":
            loop_code = translate_optimized(item[1])
            out.append((0, "while data[index]:"))
            out.extend((indent + 1, line) for indent, line in loop_code)

    return "\n".join("    " * indent + line for indent, line in out)


def transpile(sourcecode):
    optimized_code = optimize(sourcecode)
    python_code = translate_optimized(optimized_code)
    return python_code


sourcecode = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
# print(transpile(sourcecode))
print(optimize(sourcecode))
