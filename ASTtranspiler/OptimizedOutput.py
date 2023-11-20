import time
start = time.time()
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
    index += 1
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
    index += 1
    add(1)
    add(1)
    add(1)
    add(1)
    index -= 1
    subtract(1)
    # End of loop
index += 1
index += 1
add(1)
add(1)
index += 1
index += 1
index += 1
add(1)
index += 1
index += 1
index += 1
add(1)
index -= 1
index -= 1
index -= 1
index -= 1
index -= 1
index -= 1
index -= 1
index -= 1
index -= 1
index -= 1
while data[index] != 0:
    subtract(1)
    temp = data[1]
    data[1] = 0
    data[2] = temp
    index += 1
    while data[index] != 0:
        subtract(1)
        index -= 1
        add(1)
        index += 1
        index += 1
        index += 1
        output()
        index -= 1
        index -= 1
        # End of loop
    index += 1
    index += 1
    index += 1
    while data[index] != 0:
        temp = data[0]
        data[0] = 0
        data[1] = temp
            while data[index] != 0:
                index += 1
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
            index -= 1
            temp = data[15]
            data[15] = 0
            data[16] = temp
            add(1)
            index += 1
            temp = data[18]
            data[18] = 0
            data[19] = temp
            index += 1
            output()
            while data[index] != 0:
                subtract(1)
                # End of loop
            index += 1
            # End of loop
        # End of loop
    add(1)
    index -= 1
    index -= 1
    index -= 1
    while data[index] != 0:
        subtract(1)
        temp = data[1]
        data[1] = 0
        data[2] = temp
        add(1)
        index += 1
        while data[index] != 0:
            subtract(1)
            index -= 1
            add(1)
            index += 1
            index += 1
            index += 1
            subtract(1)
            temp = data[7]
            data[7] = 0
            data[8] = temp
            add(1)
            add(1)
            index += 1
            while data[index] != 0:
                subtract(1)
                index -= 1
                subtract(1)
                index += 1
                # End of loop
            index -= 1
            index -= 1
            index -= 1
            # End of loop
        index -= 1
        index -= 1
        index -= 1
        index -= 1
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
    add(1)
    add(1)
    add(1)
    output()
    while data[index] != 0:
        subtract(1)
        # End of loop
    index -= 1
    # End of loop
add(1)
add(1)
add(1)
add(1)
add(1)
end = time.time()
print(end - start)