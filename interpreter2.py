def execute_brainfuck(program_code):
    memory_cells = [0]
    memory_pointer = 0
    program_pointer = 0

    while program_pointer < len(program_code):
        command = program_code[program_pointer]

        if command == ">":
            memory_pointer += 1
            if len(memory_cells) <= memory_pointer:
                memory_cells.append(0)

        elif command == "<":
            memory_pointer -= 1
            if memory_pointer < 0:
                print("Error: Moved off memory cells array!")

        elif command == "+":
            memory_cells[memory_pointer] = (memory_cells[memory_pointer] + 1) % 256

        elif command == "-":
            memory_cells[memory_pointer] = (memory_cells[memory_pointer] - 1) % 256

        elif command == ".":
            print(chr(memory_cells[memory_pointer]), end="")

        elif command == ",":
            user_input = input("Input requested: ")
            memory_cells[memory_pointer] = ord(user_input[0])

        elif command == "[":
            if memory_cells[memory_pointer] == 0:
                opened_count = 0
                program_pointer += 1
                while program_pointer < len(program_code):
                    if program_code[program_pointer] == "]" and opened_count == 0:
                        break
                    elif program_code[program_pointer] == "[":
                        opened_count += 1
                    elif program_code[program_pointer] == "]":
                        opened_count -= 1
                    program_pointer += 1

        elif command == "]":
            if memory_cells[memory_pointer] != 0:
                closed_count = 0
                program_pointer -= 1
                while program_pointer >= 0:
                    if program_code[program_pointer] == "[" and closed_count == 0:
                        break
                    elif program_code[program_pointer] == "]":
                        closed_count += 1
                    elif program_code[program_pointer] == "[":
                        closed_count -= 1
                    program_pointer -= 1

        program_pointer += 1

if __name__ == "__main__":
    with open("brainfuck.txt", "r") as file:
        bf_program_code = file.read()

    execute_brainfuck(bf_program_code)
