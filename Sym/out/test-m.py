import sys

def main():
    tape = [0] * 30000  # Initialize tape

    tape[1] = ord(input())
    tape[0] = 3
    pointer = 1
    while tape[pointer] != 0:
        pointer += 1
        tape[pointer] = (tape[pointer] + 1)
        tape[pointer] = (tape[pointer] + 1)
        pointer -= 1
        tape[pointer] = (tape[pointer] - 1)
    
    pointer += 1
    pointer += 1
    pointer += 1
    pointer += 1
    tape[pointer] = (tape[pointer] + 1)
    tape[pointer] = (tape[pointer] + 1)
    tape[pointer] = (tape[pointer] + 1)
    tape[pointer] = (tape[pointer] + 1)
    tape[pointer] = (tape[pointer] + 1)
    pointer -= 1
    tape[pointer] = (tape[pointer] + 1)
    tape[pointer] = (tape[pointer] + 1)
    tape[pointer] = (tape[pointer] + 1)
    tape[pointer] = (tape[pointer] + 1)
    print(chr(tape[pointer]), end='')
    
    print()  # New line after program execution

if __name__ == "__main__":
    main()
        