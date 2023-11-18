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
bf_sub(1)
while data[index] != 0:
    bf_sub(3)
    index += 1
    bf_add(1)
    index -= 1
# End of loop
index += 1
bf_sub(1)
bf_output()
while data[index] != 0:
    bf_sub(4)
    index += 1
    bf_add(5)
    index -= 1
# End of loop
index += 1
bf_sub(1)
bf_output()
bf_sub(3)
bf_output()
bf_sub(2)
while data[index] != 0:
    bf_sub(3)
    index += 1
    bf_add(1)
    index -= 1
# End of loop
index += 1
bf_sub(1)
bf_output()
while data[index] != 0:
    bf_sub(2)
    index += 1
    bf_add(5)
    index -= 1
# End of loop
index += 1
bf_output()
while data[index] != 0:
    bf_sub(3)
    index += 1
    bf_add(1)
    index -= 1
# End of loop
index += 1
bf_add(2)
bf_output()
bf_sub(3)
bf_output()
bf_sub(8)
bf_output()
bf_add(11)
bf_output()
bf_add(3)
while data[index] != 0:
    bf_sub(1)
    index += 1
    bf_add(3)
    index -= 1
# End of loop
index += 1
bf_add(2)
bf_output()
bf_add(12)
bf_output()
while data[index] != 0:
    bf_sub(1)
    index += 1
    bf_add(5)
    index -= 1
# End of loop
index += 1
bf_sub(1)
bf_output()
while data[index] != 0:
    bf_sub(1)
    index += 1
    bf_add(2)
    index -= 1
# End of loop
index += 1
bf_add(1)
bf_output()
while data[index] != 0:
    bf_sub(3)
    index += 1
    bf_add(1)
    index -= 1
# End of loop
index += 1
bf_add(3)
bf_output()
bf_sub(13)
bf_output()
bf_add(11)
bf_output()
bf_sub(1)
while data[index] != 0:
    bf_sub(3)
    index += 1
    bf_add(1)
    index -= 1
# End of loop
index += 1
bf_output()
bf_sub(6)
bf_output()
bf_sub(10)
bf_output()
bf_add(10)
bf_output()
bf_add(1)
while data[index] != 0:
    bf_sub(4)
    index += 1
    bf_add(1)
    index -= 1
# End of loop
index += 1
bf_add(3)
bf_output()
bf_add(1)
while data[index] != 0:
    bf_sub(1)
    index += 1
    bf_add(3)
    index -= 1
# End of loop
index += 1
bf_output()
bf_add(12)
bf_output()
bf_add(6)
bf_output()
bf_sub(3)
bf_output()
bf_add(1)
bf_output()
bf_add(4)
while data[index] != 0:
    bf_sub(1)
    index += 1
    bf_add(3)
    index -= 1
# End of loop
index += 1
bf_output()
bf_sub(2)
while data[index] != 0:
    bf_sub(3)
    index += 1
    bf_add(1)
    index -= 1
# End of loop
index += 1
bf_sub(1)
bf_output()
bf_sub(1)
while data[index] != 0:
    bf_sub(3)
    index += 1
    bf_add(2)
    index -= 1
# End of loop
index += 1
bf_sub(1)
bf_output()
bf_add(10)
bf_output()
bf_add(1)
while data[index] != 0:
    bf_sub(4)
    index += 1
    bf_add(1)
    index -= 1
# End of loop
index += 1
bf_add(3)
bf_output()
bf_sub(1)
while data[index] != 0:
    bf_sub(3)
    index += 1
    bf_add(2)
    index -= 1
# End of loop
index += 1
bf_sub(2)
bf_output()
bf_sub(3)
bf_output()
bf_add(7)
bf_output()
bf_output()
bf_sub(11)
bf_output()
bf_sub(1)
while data[index] != 0:
    bf_sub(1)
    index += 1
    bf_add(3)
    index -= 1
# End of loop
index += 1
bf_output()
bf_sub(1)
while data[index] != 0:
    bf_sub(3)
    index += 1
    bf_add(2)
    index -= 1
# End of loop
index += 1
bf_sub(2)
bf_output()
bf_sub(7)
bf_output()
bf_sub(2)
while data[index] != 0:
    bf_sub(3)
    index += 1
    bf_add(1)
    index -= 1
# End of loop
index += 1
bf_sub(3)
bf_output()
bf_sub(14)
bf_output()
bf_add(3)