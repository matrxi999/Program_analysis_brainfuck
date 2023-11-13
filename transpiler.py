def translate(sourcecode):
    out = [
        (0, "printChar = lambda x: print(chr(x), end='')"),
        (0, "data = [0]*30000"),
        (0, "index = 0"),
        (0, "def add(x):data[index] = (data[index] + x) % 256"),
        (0, "def sub(x):data[index] = (data[index] - x) % 256"),
    ]
    level = 0
    operation = None
    for operation in sourcecode:
        if operation == "+":
            out.append((level, f"add(1)"))
        elif operation == "-":
            out.append((level, f"sub(1)"))
        elif operation == ">":
            out.append((level, f"index += 1"))
        elif operation == "<":
            out.append((level, f"index -= 1"))
        elif operation == ".":
            out.append((level, "printChar(data[index])"))
        elif operation == ",":
            out.append((level, "data[index] = ord(input())"))
        elif operation == "[":
            out.append((level, "while data[index]:"))
            level += 1
        elif operation == "]":
            if level > 0:
                level -= 1

    if level != 0:
        raise Exception("Missing closing bracket!")
    
    return "\n".join("    " * indent + line for indent, line in out)
 
python_code = translate(">++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.")

with open("Output.py", "w", encoding="utf-8") as text_file:
    text_file.write(python_code)