from collections import defaultdict
putch = lambda x: print(chr(x), end='')
data = defaultdict(int)
index = 0
def add(x):data[index] = (data[index] + x) % 256
def sub(x):data[index] = (data[index] - x) % 256
add(10)
while data[index]:
    index += 1
    add(7)
    index += 1
    add(10)
    index += 1
    add(3)
    index += 1
    add(1)
    index -= 4
    sub(1)
index += 1
add(2)
putch(data[index])
index += 1
add(1)
putch(data[index])
add(7)
putch(data[index])
putch(data[index])
add(3)
putch(data[index])
index += 1
add(2)
putch(data[index])
index -= 2
add(15)
putch(data[index])
index += 1
putch(data[index])
add(3)
putch(data[index])
sub(6)
putch(data[index])
sub(8)
putch(data[index])
index += 1
add(1)
putch(data[index])
index += 1
putch(data[index])