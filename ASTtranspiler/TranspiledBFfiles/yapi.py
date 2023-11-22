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
add(15)
while data[index] != 0:
    index -= 1
    add(1)
    index += 8
    add(10)
    index -= 7
    subtract(1)
    # End of loop
index += 1
add(5)
while data[index] != 0:
    index -= 1
    add(9)
    index += 1
    subtract(1)
    # End of loop
add(1)
index += 6
add(1)
while data[index] != 0:
    index -= 2
    add(3)
    while data[index] != 0:
        index += 2
        while data[index] != 0:
            subtract(1)
            index -= 1
            # End of loop
        index -= 1
        while data[index] != 0:
            index += 1
            # End of loop
        index -= 1
        subtract(1)
        # End of loop
    index += 2
    while data[index] != 0:
        index += 1
        add(1)
        index += 1
        # End of loop
    index -= 1
    while data[index] != 0:
        index -= 1
        # End of loop
    index += 1
    # End of loop
index += 1
while data[index] != 0:
    while data[index] != 0:
        subtract(1)
        index += 4
        add(1)
        index -= 4
        # End of loop
    index += 3
    add(3)
    index += 1
    subtract(1)
    # End of loop
index -= 1
while data[index] != 0:
    index -= 4
    # End of loop
index -= 8
add(1)
while data[index] != 0:
    subtract(1)
    index += 12
    while data[index] != 0:
        index -= 1
        add(1)
        while data[index] != 0:
            subtract(1)
            index += 4
            add(1)
            index -= 4
            # End of loop
        index += 5
        # End of loop
    index -= 4
    while data[index] != 0:
        index += 5
        while data[index] != 0:
            index -= 4
            add(1)
            index += 4
            subtract(1)
            # End of loop
        index -= 5
        subtract(1)
        while data[index] != 0:
            index -= 2
            add(10)
            index += 2
            subtract(1)
            # End of loop
        index += 3
        while data[index] != 0:
            index -= 2
            while data[index] != 0:
                index -= 1
                add(1)
                index -= 2
                add(1)
                index += 3
                subtract(1)
                # End of loop
            index -= 1
            while data[index] != 0:
                index += 1
                add(1)
                index -= 1
                subtract(1)
                # End of loop
            index -= 1
            add(2)
            index -= 2
            add(1)
            index += 6
            subtract(1)
            # End of loop
        index -= 2
        data[index] = 0
        index -= 2
        subtract(1)
        index -= 1
        while data[index] != 0:
            subtract(1)
            index += 2
            add(1)
            index -= 1
            subtract(1)
            while data[index] != 0:
                index += 3
                # End of loop
            index += 1
            while data[index] != 0:
                while data[index] != 0:
                    index -= 1
                    add(1)
                    index += 1
                    subtract(1)
                    # End of loop
                index += 1
                add(1)
                index += 2
                # End of loop
            index -= 5
            # End of loop
        index += 1
        data[index] = 0
        index += 1
        add(1)
        index -= 3
        subtract(1)
        while data[index] != 0:
            index += 2
            add(1)
            index -= 2
            subtract(1)
            # End of loop
        index -= 1
        # End of loop
    index -= 4
    add(1)
    index += 8
    data[index] = 0
    index += 1
    while data[index] != 0:
        index -= 3
        add(1)
        index += 3
        subtract(1)
        # End of loop
    index -= 2
    add(10)
    index -= 1
    while data[index] != 0:
        subtract(1)
        index += 2
        add(1)
        index -= 1
        subtract(1)
        while data[index] != 0:
            index += 3
            # End of loop
        index += 1
        while data[index] != 0:
            while data[index] != 0:
                index -= 1
                add(1)
                index += 1
                subtract(1)
                # End of loop
            index += 1
            add(1)
            index += 2
            # End of loop
        index -= 5
        # End of loop
    index += 1
    data[index] = 0
    index += 1
    add(1)
    index += 1
    while data[index] != 0:
        index -= 2
        add(1)
        index -= 1
        add(1)
        index += 3
        subtract(1)
        # End of loop
    index -= 4
    add(1)
    index -= 1
    add(1)
    index += 2
    while data[index] != 0:
        subtract(1)
        while data[index] != 0:
            subtract(1)
            while data[index] != 0:
                subtract(1)
                while data[index] != 0:
                    subtract(1)
                    while data[index] != 0:
                        subtract(1)
                        while data[index] != 0:
                            subtract(1)
                            while data[index] != 0:
                                subtract(1)
                                while data[index] != 0:
                                    subtract(1)
                                    while data[index] != 0:
                                        subtract(1)
                                        index -= 1
                                        subtract(1)
                                        index += 1
                                        while data[index] != 0:
                                            subtract(1)
                                            index -= 1
                                            add(1)
                                            index -= 1
                                            subtract(1)
                                            index += 2
                                            # End of loop
                                        # End of loop
                                    # End of loop
                                # End of loop
                            # End of loop
                        # End of loop
                    # End of loop
                # End of loop
            # End of loop
        # End of loop
    index -= 1
    while data[index] != 0:
        add(5)
        while data[index] != 0:
            index -= 3
            add(8)
            index -= 1
            add(8)
            index += 4
            subtract(1)
            # End of loop
        index -= 4
        add(1)
        index -= 1
        subtract(1)
        index += 4
        while data[index] != 0:
            index += 1
            add(1)
            index -= 3
            add(9)
            index -= 1
            subtract(1)
            index += 3
            subtract(1)
            # End of loop
        index -= 5
        while data[index] != 0:
            index += 2
            add(1)
            index -= 2
            subtract(1)
            # End of loop
        add(1)
        index -= 1
        while data[index] != 0:
            subtract(1)
            index += 1
            subtract(1)
            index -= 1
            # End of loop
        index += 1
        while data[index] != 0:
            index += 2
            output()
            index -= 4
            while data[index] != 0:
                add(1)
                output()
                data[index] = 0
                # End of loop
            index += 2
            subtract(1)
            # End of loop
        index += 1
        while data[index] != 0:
            index += 2
            output()
            index -= 2
            subtract(1)
            # End of loop
        index += 1
        data[index] = 0
        index += 1
        data[index] = 0
        index += 3
        while data[index] != 0:
            index += 2
            while data[index] != 0:
                index -= 8
                add(1)
                index += 8
                subtract(1)
                # End of loop
            index -= 2
            subtract(1)
            # End of loop
        # End of loop
    index += 2
    data[index] = 0
    index -= 3
    data[index] = 0
    index -= 8
    # End of loop
add(10)
output()
