import sys

def main():
    tape = [0] * 30000  # Initialize tape
    pointer = 0
    
    tape[0] = 1
    tape[1] = 1
    sys.stdout.write(chr(tape[0]))
    tape[0] = 1
    tape[1] = 1
    
    print()  # New line after program execution

if __name__ == "__main__":
    main()
        