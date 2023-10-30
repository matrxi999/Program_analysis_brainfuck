def translate(sourcecode):
    out = [
        (0, "from collections import defaultdict"),
        (0, "from msvcrt import getch"),
        (0, "putch = lambda x: print(chr(x), end='')"),
        (0, "data = defaultdict(int)"),
        (0, "index = 0"),
        (0, "def add(x):data[index] = (data[index] + x) % 256"),
        (0, "def sub(x):data[index] = (data[index] - x) % 256"),
    ]
    level = 0
    count = 0
    operation = None
    for c in sourcecode:
        if c == operation:
            count += 1
        else:
            if operation == "+":
                out.append((level, f"add({count!r})"))
            elif operation == "-":
                out.append((level, f"sub({count!r})"))
            elif operation == ">":
                out.append((level, f"index += {count!r}"))
            elif operation == "<":
                out.append((level, f"index -= {count!r}"))
            operation = None

            if c in "+-><":
                operation = c
                count = 1
            elif c == ".":
                out.append((level, "putch(data[index])"))
            elif c == ",":
                out.append((level, "data[index] = getch()[0]"))
            elif c == "[":
                out.append((level, "while data[index]:"))
                level += 1
            elif c == "]":
                assert level
                level -= 1
    return "\n".join("    " * indent + line for indent, line in out)

print(translate("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."))