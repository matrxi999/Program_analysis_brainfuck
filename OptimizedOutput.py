data = [0]*30000
index = 0
def bf_add(x):
    global index
    data[index] = (data[index] + x) % 256
def bf_sub(x):
    global index
    data[index] = (data[index] - x) % 256
def bf_clear():
    global index
    data[index] = 0
def bf_output():
    global index
    print(chr(data[index]), end='')
def bf_input():
    global index
    data[index] = ord(input())
def zero_cell():
    global index
    data[index] = 0
index += 2
bf_add(2)
bf_output()
bf_add(2)
while data[index] != 0:
    bf_sub(1)
    index -= 1
    bf_add(5)
    bf_output()
    bf_add(4)
    index += 1
# End of loop
index -= 1
bf_output()
while data[index] != 0:
    bf_sub(1)
    index += 1
    bf_add(2)
    index -= 1
# End of loop
index += 1
bf_add(3)
bf_output()
bf_add(2)
while data[index] != 0:
    bf_sub(1)
    index -= 1
    bf_add(5)
    index += 1
# End of loop
index -= 1
zero_cell()
index += 1
bf_output()
zero_cell()
index += 1
bf_output()
index += 1
bf_input()
bf_add(2)
bf_output()
bf_sub(4)
zero_cell()