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
add(4)
while data[index] != 0:
    index -= 1
    add(8)
    index += 1
    subtract(1)
    # End of loop
index += 1
add(8)
while data[index] != 0:
    index += 1
    add(4)
    index -= 1
    subtract(1)
    # End of loop
index += 2
add(2)
index += 3
add(1)
index += 3
add(1)
index -= 10
while data[index] != 0:
    subtract(1)
    temp = data[index]
    data[index] = 0
    data[index + 1] = temp
    index += 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        add(1)
        index += 3
        output()
        index -= 2
        # End of loop
    index += 3
    while data[index] != 0:
        while data[index] != 0:
            subtract(1)
            index += 1
            add(8)
            while data[index] != 0:
                index += 1
                add(4)
                index -= 1
                subtract(1)
                # End of loop
            index += 1
            output()
            index -= 2
            temp = data[index]
            data[index] = 0
            data[index + 1] = temp
            add(1)
            index += 1
            while data[index] != 0:
                subtract(1)
                index += 1
                add(10)
                index -= 2
                add(1)
                index += 1
                # End of loop
            index += 1
            output()
            data[index] = 0
            index += 1
            # End of loop
        # End of loop
    add(1)
    index -= 3
    while data[index] != 0:
        subtract(1)
        temp = data[index]
        data[index] = 0
        data[index + 1] = temp
        add(1)
        index += 1
        while data[index] != 0:
            subtract(1)
            index -= 1
            add(1)
            index += 3
            subtract(1)
            temp = data[index]
            data[index] = 0
            data[index + 1] = temp
            add(2)
            index += 1
            while data[index] != 0:
                subtract(1)
                index -= 1
                subtract(1)
                index += 1
                # End of loop
            index -= 3
            # End of loop
        index -= 4
        # End of loop
    add(10)
    output()
    add(3)
    output()
    data[index] = 0
    index -= 1
    # End of loop
add(5)
