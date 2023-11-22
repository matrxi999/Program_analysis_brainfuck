data = [0]*30000
index = 0
def add(x):
    global index
    data[index] = (data[index] + x) % 256
def subtract(x):
    global index
    data[index] = (data[index] - x) % 256
def output():
    global index
    print(chr(data[index]), end='')
def input_():
    global index
    data[index] = ord(input())
index += 1
add(1)
add(1)
add(1)
add(1)
add(1)
add(1)
add(1)
add(1)
add(1)
add(1)
while data[index] != 0:
    index -= 1
    add(1)
    add(1)
    add(1)
    add(1)
    add(1)
    add(1)
    add(1)
    add(1)
    add(1)
    add(1)
    index += 1
    subtract(1)
    # End of loop
index -= 1
subtract(1)
index += 1
index += 1
index += 1
index += 1
index += 1
add(1)
add(1)
add(1)
while data[index] != 0:
    index += 1
    add(1)
    add(1)
    add(1)
    index += 1
    add(1)
    add(1)
    add(1)
    index -= 1
    index -= 1
    subtract(1)
    # End of loop
index -= 1
index -= 1
index -= 1
index -= 1
add(1)
index -= 1
while data[index] != 0:
    index += 1
    while data[index] != 0:
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 1
        index -= 1
        subtract(1)
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    add(1)
    add(1)
    add(1)
    add(1)
    index += 1
    add(1)
    index -= 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        subtract(1)
        index += 1
        # End of loop
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        index += 1
        subtract(1)
        index -= 1
        index -= 1
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    index -= 1
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        index += 1
        index += 1
        index += 1
        index += 1
        index += 1
        while data[index] != 0:
            while data[index] != 0:
                subtract(1)
                # End of loop
            index -= 1
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            index -= 1
            subtract(1)
            index += 1
            index += 1
            # End of loop
        index -= 1
        subtract(1)
        while data[index] != 0:
            index += 1
            add(1)
            index += 1
            add(1)
            index -= 1
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        while data[index] != 0:
            index -= 1
            add(1)
            index += 1
            subtract(1)
            # End of loop
        add(1)
        index += 1
        while data[index] != 0:
            while data[index] != 0:
                subtract(1)
                # End of loop
            index -= 1
            subtract(1)
            index += 1
            # End of loop
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        subtract(1)
        index += 1
        index += 1
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 1
        index -= 1
        subtract(1)
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    add(1)
    index += 1
    add(1)
    index -= 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        subtract(1)
        index += 1
        # End of loop
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        index += 1
        subtract(1)
        index -= 1
        index -= 1
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    index -= 1
    index -= 1
    index -= 1
    while data[index] != 0:
        index += 1
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 1
        index -= 1
        index -= 1
        subtract(1)
        # End of loop
    index += 1
    index += 1
    index += 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        index += 1
        # End of loop
    add(1)
    add(1)
    index += 1
    add(1)
    index -= 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        subtract(1)
        index += 1
        # End of loop
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        index += 1
        subtract(1)
        index -= 1
        index -= 1
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    index -= 1
    index -= 1
    while data[index] != 0:
        index += 1
        add(1)
        index -= 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 1
        index += 1
        add(1)
        index -= 1
        index -= 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        # End of loop
    index -= 1
    index -= 1
    index -= 1
    while data[index] != 0:
        index += 1
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 1
        index -= 1
        index -= 1
        subtract(1)
        # End of loop
    index += 1
    index += 1
    index += 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        index += 1
        # End of loop
    add(1)
    add(1)
    add(1)
    add(1)
    index += 1
    add(1)
    index -= 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        subtract(1)
        index += 1
        # End of loop
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        index += 1
        subtract(1)
        index -= 1
        index -= 1
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    index -= 1
    index -= 1
    while data[index] != 0:
        index += 1
        add(1)
        index -= 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 1
        index += 1
        add(1)
        index -= 1
        index -= 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        # End of loop
    index -= 1
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        index += 1
        index += 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index += 1
            index += 1
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            index -= 1
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        while data[index] != 0:
            index -= 1
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            while data[index] != 0:
                index += 1
                add(1)
                add(1)
                add(1)
                add(1)
                add(1)
                add(1)
                index -= 1
                subtract(1)
                # End of loop
            index += 1
            output()
            index -= 1
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            while data[index] != 0:
                index += 1
                subtract(1)
                subtract(1)
                subtract(1)
                subtract(1)
                subtract(1)
                subtract(1)
                index -= 1
                subtract(1)
                # End of loop
            index += 1
            while data[index] != 0:
                index -= 1
                index -= 1
                add(1)
                index += 1
                index += 1
                subtract(1)
                # End of loop
            # End of loop
        index += 1
        output()
        index -= 1
        index -= 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index += 1
            index += 1
            subtract(1)
            subtract(1)
            subtract(1)
            subtract(1)
            subtract(1)
            subtract(1)
            index -= 1
            index -= 1
            subtract(1)
            # End of loop
        index -= 1
        while data[index] != 0:
            subtract(1)
            index += 1
            index += 1
            add(1)
            index -= 1
            index -= 1
            # End of loop
        index -= 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index -= 1
            add(1)
            add(1)
            add(1)
            add(1)
            index += 1
            subtract(1)
            # End of loop
        index -= 1
        output()
        index += 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index += 1
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        add(1)
        add(1)
        add(1)
        output()
        index -= 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index += 1
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        output()
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        index += 1
        index += 1
        while data[index] != 0:
            index += 1
            index += 1
            index += 1
            add(1)
            index += 1
            add(1)
            index -= 1
            index -= 1
            index -= 1
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        index += 1
        index += 1
        index += 1
        while data[index] != 0:
            subtract(1)
            index -= 1
            index -= 1
            index -= 1
            index -= 1
            add(1)
            index += 1
            index += 1
            index += 1
            index += 1
            # End of loop
        index += 1
        add(1)
        index -= 1
        while data[index] != 0:
            subtract(1)
            index -= 1
            subtract(1)
            index += 1
            # End of loop
        index -= 1
        while data[index] != 0:
            while data[index] != 0:
                subtract(1)
                # End of loop
            index += 1
            index += 1
            subtract(1)
            index -= 1
            index -= 1
            # End of loop
        index += 1
        index += 1
        while data[index] != 0:
            while data[index] != 0:
                subtract(1)
                # End of loop
            index -= 1
            index -= 1
            add(1)
            index += 1
            index += 1
            # End of loop
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        while data[index] != 0:
            index += 1
            index += 1
            index += 1
            add(1)
            index += 1
            add(1)
            index -= 1
            index -= 1
            index -= 1
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        index += 1
        index += 1
        index += 1
        while data[index] != 0:
            subtract(1)
            index -= 1
            index -= 1
            index -= 1
            index -= 1
            add(1)
            index += 1
            index += 1
            index += 1
            index += 1
            # End of loop
        add(1)
        index += 1
        add(1)
        index -= 1
        while data[index] != 0:
            subtract(1)
            index -= 1
            subtract(1)
            index += 1
            # End of loop
        index -= 1
        while data[index] != 0:
            while data[index] != 0:
                subtract(1)
                # End of loop
            index += 1
            index += 1
            subtract(1)
            index -= 1
            index -= 1
            # End of loop
        index += 1
        index += 1
        while data[index] != 0:
            while data[index] != 0:
                subtract(1)
                # End of loop
            index -= 1
            index -= 1
            add(1)
            index += 1
            index += 1
            # End of loop
        index -= 1
        index -= 1
        index -= 1
        while data[index] != 0:
            index += 1
            index += 1
            add(1)
            index -= 1
            index -= 1
            while data[index] != 0:
                subtract(1)
                # End of loop
            # End of loop
        index += 1
        while data[index] != 0:
            index += 1
            add(1)
            index -= 1
            while data[index] != 0:
                subtract(1)
                # End of loop
            # End of loop
        add(1)
        add(1)
        index += 1
        index += 1
        add(1)
        index -= 1
        while data[index] != 0:
            subtract(1)
            index -= 1
            subtract(1)
            index += 1
            # End of loop
        index -= 1
        while data[index] != 0:
            while data[index] != 0:
                subtract(1)
                # End of loop
            index += 1
            index += 1
            subtract(1)
            index -= 1
            index -= 1
            # End of loop
        index += 1
        index += 1
        while data[index] != 0:
            while data[index] != 0:
                subtract(1)
                # End of loop
            index -= 1
            index -= 1
            add(1)
            index += 1
            index += 1
            # End of loop
        index -= 1
        add(1)
        index -= 1
        while data[index] != 0:
            while data[index] != 0:
                subtract(1)
                # End of loop
            index += 1
            subtract(1)
            index -= 1
            # End of loop
        index += 1
        while data[index] != 0:
            index -= 1
            index -= 1
            index -= 1
            index -= 1
            index -= 1
            index -= 1
            index -= 1
            output()
            index += 1
            index += 1
            index += 1
            index += 1
            index += 1
            index += 1
            index += 1
            while data[index] != 0:
                subtract(1)
                # End of loop
            # End of loop
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        index -= 1
        output()
        index += 1
        index += 1
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        index -= 1
        index -= 1
        output()
        index += 1
        index += 1
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        add(1)
        add(1)
        add(1)
        output()
        output()
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        while data[index] != 0:
            subtract(1)
            # End of loop
        index -= 1
        index -= 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 1
        index -= 1
        subtract(1)
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    add(1)
    index += 1
    add(1)
    index -= 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        subtract(1)
        index += 1
        # End of loop
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        index += 1
        subtract(1)
        index -= 1
        index -= 1
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    index -= 1
    index -= 1
    index -= 1
    while data[index] != 0:
        index += 1
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 1
        index -= 1
        index -= 1
        subtract(1)
        # End of loop
    index += 1
    index += 1
    index += 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        index += 1
        # End of loop
    add(1)
    add(1)
    add(1)
    add(1)
    index += 1
    add(1)
    index -= 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        subtract(1)
        index += 1
        # End of loop
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        index += 1
        subtract(1)
        index -= 1
        index -= 1
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    index -= 1
    index -= 1
    while data[index] != 0:
        index += 1
        add(1)
        index -= 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 1
        index += 1
        add(1)
        index -= 1
        index -= 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        # End of loop
    index -= 1
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index -= 1
            add(1)
            add(1)
            add(1)
            add(1)
            index += 1
            subtract(1)
            # End of loop
        index -= 1
        output()
        index += 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index += 1
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        add(1)
        output()
        subtract(1)
        output()
        index -= 1
        index -= 1
        output()
        index += 1
        index += 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        index -= 1
        index -= 1
        output()
        index += 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index += 1
            add(1)
            add(1)
            add(1)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        output()
        index -= 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index += 1
            subtract(1)
            subtract(1)
            subtract(1)
            subtract(1)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        add(1)
        add(1)
        output()
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        output()
        while data[index] != 0:
            subtract(1)
            # End of loop
        index -= 1
        index -= 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        while data[index] != 0:
            subtract(1)
            # End of loop
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 1
        index -= 1
        subtract(1)
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    add(1)
    add(1)
    add(1)
    index += 1
    add(1)
    index -= 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        subtract(1)
        index += 1
        # End of loop
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        index += 1
        subtract(1)
        index -= 1
        index -= 1
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    index -= 1
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        index += 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index += 1
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        add(1)
        add(1)
        add(1)
        output()
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        index -= 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index += 1
            index += 1
            add(1)
            add(1)
            add(1)
            add(1)
            index -= 1
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        index += 1
        output()
        index -= 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        subtract(1)
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        index += 1
        output()
        index -= 1
        subtract(1)
        output()
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        index += 1
        output()
        index -= 1
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        index += 1
        output()
        index -= 1
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        index -= 1
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index += 1
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            add(1)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        output()
        output()
        index += 1
        output()
        index -= 1
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        index += 1
        output()
        index -= 1
        index -= 1
        add(1)
        add(1)
        add(1)
        while data[index] != 0:
            index += 1
            subtract(1)
            subtract(1)
            subtract(1)
            subtract(1)
            subtract(1)
            subtract(1)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        subtract(1)
        output()
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        subtract(1)
        output()
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        index -= 1
        index -= 1
        index -= 1
        output()
        while data[index] != 0:
            subtract(1)
            # End of loop
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 1
        index -= 1
        subtract(1)
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    add(1)
    add(1)
    add(1)
    add(1)
    index += 1
    add(1)
    index -= 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        subtract(1)
        index += 1
        # End of loop
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        index += 1
        subtract(1)
        index -= 1
        index -= 1
        # End of loop
    index += 1
    index += 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        index -= 1
        index -= 1
        add(1)
        index += 1
        index += 1
        # End of loop
    index -= 1
    index -= 1
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            # End of loop
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        add(1)
        output()
        while data[index] != 0:
            subtract(1)
            # End of loop
        index -= 1
        while data[index] != 0:
            subtract(1)
            # End of loop
        index += 1
        # End of loop
    index -= 1
    add(1)
    index -= 1
    # End of loop
