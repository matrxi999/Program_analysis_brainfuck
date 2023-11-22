import sys

def main():
    tape = [0] * 30000  # Initialize tape
    pointer = 0

    tape[0] = 72
    print(chr(tape[0]), end='')
    tape[0] = 101
    print(chr(tape[0]), end='')
    tape[0] = 108
    print(chr(tape[0]), end='')
    print(chr(tape[0]), end='')
    tape[0] = 111
    print(chr(tape[0]), end='')
    tape[1] = 44
    print(chr(tape[1]), end='')
    tape[1] = 32
    print(chr(tape[1]), end='')
    tape[1] = 87
    print(chr(tape[1]), end='')
    print(chr(tape[0]), end='')
    tape[0] = 114
    print(chr(tape[0]), end='')
    tape[0] = 108
    print(chr(tape[0]), end='')
    tape[0] = 100
    print(chr(tape[0]), end='')
    tape[2] = 33
    print(chr(tape[2]), end='')
    
    print()  # New line after program execution

if __name__ == "__main__":
    main()
        