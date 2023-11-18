data = [0]*30000
index = 0
def bf_add(x):
    global index
    data[index] = (data[index] + x) % 256
def bf_sub(x):
    global index
    data[index] = (data[index] - x) % 256
def bf_output():
    global index
    print(chr(data[index]), end='')
def bf_input():
    global index
    data[index] = ord(input())
index += 1
while data[index] != 0:
    index -= 1
    index += 1
    # End of loop
index -= 1
bf_output()
index += 1
while data[index] != 0:
    index -= 1
    index += 1
    # End of loop
index -= 1
bf_output()
bf_output()
bf_output()
bf_output()
index += 1
index += 1
while data[index] != 0:
    index -= 1
    index += 1
    # End of loop
index -= 1
bf_output()
bf_output()
index += 1
while data[index] != 0:
    index -= 1
    index += 1
    # End of loop
index -= 1
bf_output()
index -= 1
bf_output()
bf_output()
bf_output()
bf_output()
index += 1
index += 1
index += 1
while data[index] != 0:
    index -= 1
    index += 1
    # End of loop
index -= 1
bf_output()