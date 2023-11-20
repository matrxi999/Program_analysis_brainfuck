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
temp = data[0]
data[0] = 0
data[1] = temp
data[2] = temp
while data[index] != 0:
    subtract(1)
    index += 1
    add(1)
    index += 1
    add(1)
    index -= 2
    # End of loop
add(10)
while data[index] != 0:
    index += 1
    add(7)
    index += 1
    add(10)
    index += 1
    add(3)
    index += 1
    add(1)
    index -= 4
    subtract(1)
    # End of loop
index += 1
add(2)
output()
index += 1
add(1)
output()
add(7)
output()
output()
add(3)
output()
index += 1
add(2)
output()
index -= 2
add(15)
output()
index += 1
output()
add(3)
output()
subtract(6)
output()
subtract(8)
output()
index += 1
add(1)
output()
index += 1
output()