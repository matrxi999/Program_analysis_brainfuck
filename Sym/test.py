import sys

def main():
    tape = [0] * 30000  # Initialize tape
    pointer = 0

    print(chr(tape[0]), end='')
    print(chr(tape[1]), end='')
    tape[0] = 1
    tape[1] = 0
    
    print()  # New line after program execution

if __name__ == "__main__":
    main()
        