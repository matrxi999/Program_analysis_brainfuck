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
add(10)
while data[index] != 0:
    index -= 1
    add(10)
    index += 1
    subtract(1)
    # End of loop
index -= 1
subtract(1)
index += 5
add(3)
while data[index] != 0:
    index += 1
    add(3)
    index += 1
    add(3)
    index -= 2
    subtract(1)
    # End of loop
index -= 4
add(1)
index -= 1
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
    index += 2
    while data[index] != 0:
        subtract(1)
        index -= 2
        add(1)
        index += 2
        # End of loop
    add(4)
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
        data[index] = 0
        index += 2
        subtract(1)
        index -= 2
        # End of loop
    index += 2
    while data[index] != 0:
        data[index] = 0
        index -= 2
        add(1)
        index += 2
        # End of loop
    index -= 2
    while data[index] != 0:
        data[index] = 0
        index += 6
        while data[index] != 0:
            data[index] = 0
            index -= 1
            add(10)
            index -= 1
            subtract(1)
            index += 2
            # End of loop
        index -= 1
        subtract(1)
        while data[index] != 0:
            index += 1
            add(1)
            index += 1
            add(1)
            index -= 2
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
            data[index] = 0
            index -= 1
            subtract(1)
            index += 1
            # End of loop
        index -= 9
        subtract(1)
        index += 2
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 2
        subtract(1)
        # End of loop
    index += 2
    while data[index] != 0:
        subtract(1)
        index -= 2
        add(1)
        index += 2
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
        data[index] = 0
        index += 2
        subtract(1)
        index -= 2
        # End of loop
    index += 2
    while data[index] != 0:
        data[index] = 0
        index -= 2
        add(1)
        index += 2
        # End of loop
    index -= 3
    while data[index] != 0:
        index += 2
        add(1)
        index += 1
        add(1)
        index -= 3
        subtract(1)
        # End of loop
    index += 3
    while data[index] != 0:
        subtract(1)
        index -= 3
        add(1)
        index += 3
        # End of loop
    add(2)
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
        data[index] = 0
        index += 2
        subtract(1)
        index -= 2
        # End of loop
    index += 2
    while data[index] != 0:
        data[index] = 0
        index -= 2
        add(1)
        index += 2
        # End of loop
    index -= 2
    while data[index] != 0:
        index += 1
        add(1)
        index -= 1
        data[index] = 0
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 2
        add(1)
        index -= 2
        data[index] = 0
        # End of loop
    index += 2
    while data[index] != 0:
        index -= 2
        add(1)
        index += 2
        data[index] = 0
        # End of loop
    index -= 3
    while data[index] != 0:
        index += 2
        add(1)
        index += 1
        add(1)
        index -= 3
        subtract(1)
        # End of loop
    index += 3
    while data[index] != 0:
        subtract(1)
        index -= 3
        add(1)
        index += 3
        # End of loop
    add(4)
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
        data[index] = 0
        index += 2
        subtract(1)
        index -= 2
        # End of loop
    index += 2
    while data[index] != 0:
        data[index] = 0
        index -= 2
        add(1)
        index += 2
        # End of loop
    index -= 2
    while data[index] != 0:
        index += 1
        add(1)
        index -= 1
        data[index] = 0
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 2
        add(1)
        index -= 2
        data[index] = 0
        # End of loop
    index += 2
    while data[index] != 0:
        index -= 2
        add(1)
        index += 2
        data[index] = 0
        # End of loop
    index -= 2
    while data[index] != 0:
        data[index] = 0
        index += 3
        add(8)
        while data[index] != 0:
            index += 2
            add(6)
            index -= 2
            subtract(1)
            # End of loop
        index += 1
        while data[index] != 0:
            index -= 1
            add(8)
            while data[index] != 0:
                index += 1
                add(6)
                index -= 1
                subtract(1)
                # End of loop
            index += 1
            output()
            index -= 1
            add(8)
            while data[index] != 0:
                index += 1
                subtract(6)
                index -= 1
                subtract(1)
                # End of loop
            index += 1
            while data[index] != 0:
                index -= 2
                add(1)
                index += 2
                subtract(1)
                # End of loop
            # End of loop
        index += 1
        output()
        index -= 2
        add(8)
        while data[index] != 0:
            index += 2
            subtract(6)
            index -= 2
            subtract(1)
            # End of loop
        index -= 1
        while data[index] != 0:
            subtract(1)
            index += 2
            add(1)
            index -= 2
            # End of loop
        index -= 1
        add(8)
        while data[index] != 0:
            index -= 1
            add(4)
            index += 1
            subtract(1)
            # End of loop
        index -= 1
        output()
        index += 1
        add(7)
        while data[index] != 0:
            index += 1
            add(9)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        add(3)
        output()
        index -= 1
        add(5)
        while data[index] != 0:
            index += 1
            add(9)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        output()
        add(5)
        output()
        output()
        subtract(8)
        output()
        subtract(7)
        output()
        add(14)
        index += 2
        while data[index] != 0:
            index += 3
            add(1)
            index += 1
            add(1)
            index -= 4
            subtract(1)
            # End of loop
        index += 4
        while data[index] != 0:
            subtract(1)
            index -= 4
            add(1)
            index += 4
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
            data[index] = 0
            index += 2
            subtract(1)
            index -= 2
            # End of loop
        index += 2
        while data[index] != 0:
            data[index] = 0
            index -= 2
            add(1)
            index += 2
            # End of loop
        index -= 4
        while data[index] != 0:
            index += 3
            add(1)
            index += 1
            add(1)
            index -= 4
            subtract(1)
            # End of loop
        index += 4
        while data[index] != 0:
            subtract(1)
            index -= 4
            add(1)
            index += 4
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
            data[index] = 0
            index += 2
            subtract(1)
            index -= 2
            # End of loop
        index += 2
        while data[index] != 0:
            data[index] = 0
            index -= 2
            add(1)
            index += 2
            # End of loop
        index -= 3
        while data[index] != 0:
            index += 2
            add(1)
            index -= 2
            data[index] = 0
            # End of loop
        index += 1
        while data[index] != 0:
            index += 1
            add(1)
            index -= 1
            data[index] = 0
            # End of loop
        add(2)
        index += 2
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
            data[index] = 0
            index += 2
            subtract(1)
            index -= 2
            # End of loop
        index += 2
        while data[index] != 0:
            data[index] = 0
            index -= 2
            add(1)
            index += 2
            # End of loop
        index -= 1
        add(1)
        index -= 1
        while data[index] != 0:
            data[index] = 0
            index += 1
            subtract(1)
            index -= 1
            # End of loop
        index += 1
        while data[index] != 0:
            index -= 7
            output()
            index += 7
            data[index] = 0
            # End of loop
        index -= 9
        output()
        index += 2
        subtract(4)
        output()
        subtract(9)
        output()
        index -= 2
        output()
        index += 2
        subtract(4)
        output()
        add(3)
        output()
        output()
        add(13)
        output()
        data[index] = 0
        index -= 2
        data[index] = 0
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 2
        subtract(1)
        # End of loop
    index += 2
    while data[index] != 0:
        subtract(1)
        index -= 2
        add(1)
        index += 2
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
        data[index] = 0
        index += 2
        subtract(1)
        index -= 2
        # End of loop
    index += 2
    while data[index] != 0:
        data[index] = 0
        index -= 2
        add(1)
        index += 2
        # End of loop
    index -= 3
    while data[index] != 0:
        index += 2
        add(1)
        index += 1
        add(1)
        index -= 3
        subtract(1)
        # End of loop
    index += 3
    while data[index] != 0:
        subtract(1)
        index -= 3
        add(1)
        index += 3
        # End of loop
    add(4)
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
        data[index] = 0
        index += 2
        subtract(1)
        index -= 2
        # End of loop
    index += 2
    while data[index] != 0:
        data[index] = 0
        index -= 2
        add(1)
        index += 2
        # End of loop
    index -= 2
    while data[index] != 0:
        index += 1
        add(1)
        index -= 1
        data[index] = 0
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 2
        add(1)
        index -= 2
        data[index] = 0
        # End of loop
    index += 2
    while data[index] != 0:
        index -= 2
        add(1)
        index += 2
        data[index] = 0
        # End of loop
    index -= 2
    while data[index] != 0:
        data[index] = 0
        index += 1
        add(8)
        while data[index] != 0:
            index -= 1
            add(4)
            index += 1
            subtract(1)
            # End of loop
        index -= 1
        output()
        index += 1
        add(10)
        while data[index] != 0:
            index += 1
            add(11)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        add(1)
        output()
        subtract(1)
        output()
        index -= 2
        output()
        index += 2
        add(6)
        output()
        subtract(12)
        output()
        subtract(3)
        output()
        index -= 2
        output()
        index += 1
        add(6)
        while data[index] != 0:
            index += 1
            add(3)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        output()
        index -= 1
        add(6)
        while data[index] != 0:
            index += 1
            subtract(4)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        add(2)
        output()
        add(11)
        output()
        output()
        data[index] = 0
        index -= 2
        data[index] = 0
        add(10)
        output()
        data[index] = 0
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 2
        subtract(1)
        # End of loop
    index += 2
    while data[index] != 0:
        subtract(1)
        index -= 2
        add(1)
        index += 2
        # End of loop
    add(3)
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
        data[index] = 0
        index += 2
        subtract(1)
        index -= 2
        # End of loop
    index += 2
    while data[index] != 0:
        data[index] = 0
        index -= 2
        add(1)
        index += 2
        # End of loop
    index -= 2
    while data[index] != 0:
        data[index] = 0
        add(10)
        output()
        index += 1
        add(9)
        while data[index] != 0:
            index += 1
            add(9)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        add(3)
        output()
        add(13)
        output()
        add(10)
        output()
        subtract(6)
        output()
        index -= 1
        add(8)
        while data[index] != 0:
            index += 2
            add(4)
            index -= 2
            subtract(1)
            # End of loop
        index += 2
        output()
        index -= 1
        add(10)
        output()
        subtract(1)
        output()
        subtract(9)
        output()
        index += 1
        output()
        index -= 1
        subtract(1)
        output()
        add(11)
        output()
        add(8)
        output()
        subtract(9)
        output()
        index += 1
        output()
        index -= 1
        subtract(13)
        output()
        add(13)
        output()
        subtract(10)
        output()
        index += 1
        output()
        index -= 1
        add(12)
        output()
        subtract(15)
        output()
        index -= 1
        add(3)
        while data[index] != 0:
            index += 1
            add(6)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        output()
        output()
        index += 1
        output()
        index -= 1
        subtract(10)
        output()
        add(11)
        output()
        index += 1
        output()
        index -= 2
        add(3)
        while data[index] != 0:
            index += 1
            subtract(6)
            index -= 1
            subtract(1)
            # End of loop
        index += 1
        subtract(1)
        output()
        add(17)
        output()
        subtract(3)
        output()
        add(6)
        output()
        subtract(7)
        output()
        subtract(10)
        output()
        data[index] = 0
        index += 1
        data[index] = 0
        index -= 3
        output()
        data[index] = 0
        # End of loop
    index -= 1
    while data[index] != 0:
        index += 1
        add(1)
        index += 1
        add(1)
        index -= 2
        subtract(1)
        # End of loop
    index += 2
    while data[index] != 0:
        subtract(1)
        index -= 2
        add(1)
        index += 2
        # End of loop
    add(4)
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
        data[index] = 0
        index += 2
        subtract(1)
        index -= 2
        # End of loop
    index += 2
    while data[index] != 0:
        data[index] = 0
        index -= 2
        add(1)
        index += 2
        # End of loop
    index -= 2
    while data[index] != 0:
        data[index] = 0
        add(10)
        output()
        data[index] = 0
        index -= 1
        data[index] = 0
        index += 1
        # End of loop
    index -= 1
    add(1)
    index -= 1
    # End of loop
