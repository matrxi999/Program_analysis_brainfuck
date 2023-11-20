def add(index, amount):
    data[index] = (data[index] + amount) % 256

def subtract(index, amount):
    data[index] = (data[index] - amount) % 256

def output(index):
    print(chr(data[index]), end='')

def input(index):
    data[index] = ord(input())

data = [0] * 30000

add(1, 1)
add(1, 1)
add(1, 1)
add(1, 1)
add(1, 1)
add(1, 1)
add(1, 1)
add(2, 1)
add(2, 1)
add(2, 1)
add(2, 1)
add(2, 1)
add(2, 1)
add(2, 1)
add(2, 1)
add(2, 1)
add(2, 1)
add(3, 1)
add(3, 1)
add(3, 1)
add(4, 1)
subtract(0, 1)