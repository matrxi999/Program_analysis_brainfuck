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
input_()
index -= 2
index += 2
while data[index] != 0:
    add(3)
    subtract(5)
    # End of loop
index += 1
add(8)
while data[index] != 0:
    index -= 1
    add(9)
    index += 1
    subtract(1)
    # End of loop
index -= 1
output()
index += 1
add(4)
while data[index] != 0:
    index -= 1
    add(7)
    index += 1
    subtract(1)
    # End of loop
index -= 1
add(1)
output()
add(7)
output()
output()
add(3)
output()
index += 2
add(6)
while data[index] != 0:
    index -= 1
    add(7)
    index += 1
    subtract(1)
    # End of loop
index -= 1
add(2)
output()
subtract(12)
output()
index += 1
add(6)
while data[index] != 0:
    index -= 1
    add(9)
    index += 1
    subtract(1)
    # End of loop
index -= 1
add(1)
output()
index -= 1
output()
add(3)
output()
subtract(6)
output()
subtract(8)
output()
index += 3
add(4)
while data[index] != 0:
    index -= 1
    add(8)
    index += 1
    subtract(1)
    # End of loop
index -= 1
add(1)
output()