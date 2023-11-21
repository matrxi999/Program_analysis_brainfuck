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
add(2)
while data[index] != 0:
    add(1)
    temp = data[index]
    data[index] = 0
    data[index + 1] = temp
    # End of loop
subtract(2)
end = time.time()
print(end - start)