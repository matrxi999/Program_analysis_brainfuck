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
add(4)
while data[index] != 0:
    index += 1
    add(5)
    index -= 1
    subtract(1)
    # End of loop
index += 1
while data[index] != 0:
    index -= 1
    add(5)
    index += 1
    subtract(1)
    # End of loop
add(1)
index -= 1
add(1)
while data[index] != 0:
    index += 1
    while data[index] != 0:
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 2
        subtract(1)
        # End of loop
    add(2)
    index += 2
    while data[index] != 0:
        index -= 2
        add(1)
        index += 2
        subtract(1)
        # End of loop
    index += 3
    data[index] = 0
    add(2)
    index += 1
    data[index] = 0
    add(1)
    index += 3
    add(1)
    while data[index] != 0:
        data[index] = 0
        add(6)
        index += 3
        # End of loop
    index -= 3
    while data[index] != 0:
        while data[index] != 0:
            index -= 1
            add(8)
            index -= 1
            add(2)
            index += 2
            subtract(1)
            # End of loop
        add(1)
        index -= 1
        output()
        index -= 1
        while data[index] != 0:
            index += 1
            subtract(4)
            index -= 1
            subtract(1)
            # End of loop
        index -= 1
        # End of loop
    index -= 2
    while data[index] != 0:
        index += 5
        while data[index] != 0:
            index += 3
            data[index] = 0
            add(9)
            index -= 1
            while data[index] != 0:
                index += 1
                subtract(1)
                index -= 1
                subtract(1)
                # End of loop
            add(9)
            index += 1
            while data[index] != 0:
                subtract(1)
                while data[index] != 0:
                    index -= 1
                    subtract(1)
                    index += 1
                    subtract(1)
                    # End of loop
                add(1)
                while data[index] != 0:
                    index -= 3
                    # End of loop
                # End of loop
            index -= 1
            while data[index] != 0:
                index += 1
                add(1)
                index -= 1
                subtract(1)
                # End of loop
            index += 1
            # End of loop
        index -= 2
        subtract(1)
        # End of loop
    index -= 2
    subtract(1)
    # End of loop
