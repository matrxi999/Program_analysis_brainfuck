tape = [0] * 30000
ptr = 0
def bf_add(x): global ptr; tape[ptr] = (tape[ptr] + x) % 256
def bf_sub(x): global ptr; tape[ptr] = (tape[ptr] - x) % 256
def bf_output(): print(chr(tape[ptr]), end='')
def bf_input(): global ptr; tape[ptr] = ord(input('Input a character: ')[0])
ptr += 1
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
while tape[ptr] != 0:
    ptr -= 1
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    ptr += 1
    bf_sub(1)
ptr -= 1
bf_output()
ptr += 1
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
while tape[ptr] != 0:
    ptr -= 1
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    ptr += 1
    bf_sub(1)
ptr -= 1
bf_add(1)
bf_output()
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
bf_output()
bf_output()
bf_add(1)
bf_add(1)
bf_add(1)
bf_output()
ptr += 1
ptr += 1
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
while tape[ptr] != 0:
    ptr -= 1
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    ptr += 1
    bf_sub(1)
ptr -= 1
bf_add(1)
bf_add(1)
bf_output()
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_output()
ptr += 1
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
while tape[ptr] != 0:
    ptr -= 1
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    ptr += 1
    bf_sub(1)
ptr -= 1
bf_add(1)
bf_output()
ptr -= 1
bf_output()
bf_add(1)
bf_add(1)
bf_add(1)
bf_output()
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_output()
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_sub(1)
bf_output()
ptr += 1
ptr += 1
ptr += 1
bf_add(1)
bf_add(1)
bf_add(1)
bf_add(1)
while tape[ptr] != 0:
    ptr -= 1
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    bf_add(1)
    ptr += 1
    bf_sub(1)
ptr -= 1
bf_add(1)
bf_output()