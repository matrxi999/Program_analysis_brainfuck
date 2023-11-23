import copy
import os
import time
import sympy as sp

class SymbolicValue:
    def __init__(self, initial_value=None, symbolic='x'):
        self.symbol = sp.Symbol(symbolic)
        if initial_value is None:
            self.expr = self.symbol
            self.is_changed = False
        else:
            # Was changed from + or -
            self.expr = self.symbol + initial_value
            self.is_changed = True

    def get_concrete_val(self):
        concrete, _ = self.expr.as_coeff_Add()
        return int(concrete)

    def reset(self):
        self.expr = self.symbol
    def copy(self):
        # Create a new instance with the same state
        new_copy = SymbolicValue(symbolic=str(self.symbol))
        new_copy.expr = self.expr
        new_copy.is_changed = self.is_changed
        return new_copy

    def __add__(self, n):
        return SymbolicValue(symbolic=str(self.symbol), initial_value=self.get_concrete_val() + n)

    def __sub__(self, n):
        # Creating a new instance with the updated expression
        return SymbolicValue(symbolic=str(self.symbol), initial_value=self.get_concrete_val() - n)

    def __str__(self):
        return str(self.expr)


class BrainfuckSymbolicSolver:
    def __init__(self):
        self.tape = [0 for _ in range(3000)]  # tape of size 3000
        self.pointer = 0
        self.loop_stack = []  # to keep track of loop
        self.last_state = [0 for _ in range(3000)]
        self.loop_map = {}
        self.dump = False

    def clear(self):
        self.tape = [0 for _ in range(3000)]
        self.pointer = 0
        self.loop_stack = []
        self.last_state = [0 for _ in range(3000)]
        self.loop_map = {}

    def handle_loop_start(self, index, loop_end):
        if isinstance(self.tape[self.pointer], int):
            if self.tape[self.pointer] == 0:
                return loop_end  # Go to loop end
            else:
                self.loop_stack.append(self.pointer)
                return index
        elif isinstance(self.tape[self.pointer], SymbolicValue):
            self.dump = True
            return index-1
        return index

    def handle_loop_end(self, index, loop_start):
        if isinstance(self.tape[self.pointer], int):
            if self.tape[self.pointer] != 0:
                return loop_start
            else:
                self.loop_stack.pop()
                return index
        elif isinstance(self.tape[self.pointer], SymbolicValue):
            self.dump = True
            return loop_start-1
        return index
    def execute_command(self, char):
        # Execute a single Brainfuck command
        if char == '>':
            self.pointer += 1
        elif char == '<':
            self.pointer -= 1
        elif char == '+':
            if self.tape[self.pointer] == 255:
                self.tape[self.pointer] = 0
            else:
                self.tape[self.pointer] += 1
        elif char == '-':
            if self.tape[self.pointer] == 0:
                self.tape[self.pointer] = 0
            else:
                self.tape[self.pointer] -= 1

    def execute_loops(self, char, index, code):
        if char == '[':
            loop_end = self.loop_map[index]
            return self.handle_loop_start(index, loop_end)
        elif char == ']':
            loop_start = self.loop_map[index]
            return self.handle_loop_end(index, loop_start)

    def optimize(self, code):
        optimized_code = ""
        self.pointer = 0
        index = 0
        add_tab = 0
        while index < len(code):
            char = code[index]
            #print(f'Pointer = {self.pointer}, index = {index}, value = {self.tape[self.pointer]}, char = {char} ')
            if self.dump:
                if char == '>':
                    optimized_code += add_tab*"    "+"pointer += 1\n"
                
                elif char == '<':
                    optimized_code += add_tab*"    "+"pointer -= 1\n"
                    
                elif char == '+':
                    optimized_code += add_tab*"    "+"tape[pointer] = (tape[pointer] + 1)\n" 

                elif char == '-':
                    optimized_code += add_tab*"    "+"tape[pointer] = (tape[pointer] - 1)\n" 

                elif char == '.':
                    optimized_code += add_tab*"    "+"print(chr(tape[pointer]), end='')\n"

                elif char == ',':
                    optimized_code += add_tab*"    "+"tape[pointer] = ord(input('Input a character: ')[0])\n"

                elif char == '[':   
                    optimized_code += add_tab*"    "+"while tape[pointer] != 0:\n"
                    add_tab += 1

                elif char == ']':
                    add_tab-=1
                    optimized_code += "\n"
            else:
                if char in ['+', '-', '>', '<']:
                    self.execute_command(char)
                elif char == '[':
                    index = self.execute_loops(char, index, code)
                    if self.dump:
                        optimized_code += self.apply_optimizations()
                        optimized_code += f"pointer = {self.pointer}\n"
                elif char == ']':
                    index = self.execute_loops(char, index, code)
                    if self.dump:
                        optimized_code += self.apply_optimizations()
                        optimized_code += f"pointer = {self.pointer}\n"
                elif char == '.':
                    optimized_code += self.optimize_print()
                    # had_to_trans = True
                    optimized_code += f"print(chr(tape[{self.pointer}]), end='')\n"
                elif char == ',':
                    optimized_code += f"tape[{self.pointer}] = ord(input())\n"
                    self.tape[self.pointer] = SymbolicValue()

            index += 1

        if not self.dump:
            optimized_code += self.apply_optimizations()
        return optimized_code
    
    def optimize_print(self):
        optimized_code = ""
        if all(x == 0 for x in self.last_state):
            if isinstance(self.tape[self.pointer], SymbolicValue):
                if self.tape[self.pointer].get_concrete_val() != 0:
                    optimized_code += f"tape[{self.pointer}] += {self.tape[self.pointer].get_concrete_val()}\n"
                    self.last_state[self.pointer] = self.tape[self.pointer].copy()

            else:
                optimized_code += f"tape[{self.pointer}] = {self.tape[self.pointer]}\n"
                self.last_state[self.pointer] = self.tape[self.pointer]
            
        else:
            if isinstance(self.tape[self.pointer], SymbolicValue) and isinstance(self.last_state[self.pointer],SymbolicValue):
                # was and still is symbolic
                if self.tape[self.pointer].is_changed:
                    diff = self.tape[self.pointer].get_concrete_val() - self.last_state[self.pointer].get_concrete_val()
                    if diff<0:
                        optimized_code += f"tape[{self.pointer}] -= {abs(diff)}\n"
                    elif diff!=0:
                        optimized_code += f"tape[{self.pointer}] += {diff}\n"
                    self.last_state[self.pointer] = self.tape[self.pointer].copy()
                    self.tape[self.pointer].is_changed = False
            elif isinstance(self.tape[self.pointer], SymbolicValue):
                # current is symbolic - prev was concrete
                if self.tape[self.pointer].get_concrete_val() != 0:
                    optimized_code += f"tape[{self.pointer}] += {self.tape[self.pointer].get_concrete_val()}\n"
                    self.last_state[self.pointer] = self.tape[self.pointer].copy()
            elif isinstance(self.last_state[self.pointer], SymbolicValue):
                # previous was symbolic - now is conrete
                optimized_code += f"tape[{self.pointer}] = {self.tape[self.pointer]}\n"
                self.last_state[self.pointer] = self.tape[self.pointer]
            else:
                # always was concrete
                if (self.tape[self.pointer] != self.last_state[self.pointer]):
                    optimized_code += f"tape[{self.pointer}] = {self.tape[self.pointer]}\n"
                    self.last_state[self.pointer] = self.tape[self.pointer]
            
        return optimized_code

    def apply_optimizations(self):
        optimized_code = ""
        for pointer in range(len(self.tape)):

            if all(x == 0 for x in self.last_state):
                if self.tape[pointer] == 0:
                    continue
                if isinstance(self.tape[pointer], SymbolicValue):
                    # Is a symbolic expression
                    if self.tape[pointer].get_concrete_val() != 0:
                        optimized_code += f"tape[{pointer}] += {self.tape[pointer].get_concrete_val()}\n"
                else:
                    # Is a concrete value
                    optimized_code += f"tape[{pointer}] = {self.tape[pointer]}\n"
            else:
                if isinstance(self.tape[pointer], SymbolicValue) and isinstance(self.last_state[pointer],
                                                                                SymbolicValue):
                    # was and still is symbolic
                    if self.tape[pointer].is_changed:
                        diff = self.tape[pointer].get_concrete_val() - self.last_state[pointer].get_concrete_val()
                        if diff<0:
                            optimized_code += f"tape[{pointer}] -= {abs(diff)}\n"
                        elif diff!=0:
                            optimized_code += f"tape[{pointer}] += {diff}\n"
                        self.last_state[pointer] = self.tape[pointer].copy()
                        self.tape[pointer].is_changed = False
                elif isinstance(self.tape[pointer], SymbolicValue):
                    # current is symbolic - prev was concrete
                    if self.tape[pointer].get_concrete_val() != 0:
                        optimized_code += f"tape[{pointer}] += {self.tape[pointer].get_concrete_val()}\n"
                elif isinstance(self.last_state[pointer], SymbolicValue):
                    # previous was symbolic - now is conrete
                    optimized_code += f"tape[{pointer}] = {self.tape[pointer]}\n"
                else:
                    # always was concrete
                    if (self.tape[pointer] != self.last_state[pointer]):
                        optimized_code += f"tape[{pointer}] = {self.tape[pointer]}\n"

        return optimized_code

    def preprocess_loops(self, code):
        loop_map = {}
        loop_stack = []

        for i, char in enumerate(code):
            if char == '[':
                loop_stack.append(i)
            elif char == ']':
                if len(loop_stack) == 0:
                    raise ValueError(f"Unmatched ']' at position {i}")
                start_index = loop_stack.pop()
                loop_map[start_index] = i
                loop_map[i] = start_index

        if len(loop_stack) > 0:
            raise ValueError(f"Unmatched '[' at position {loop_stack[-1]}")

        return loop_map
    def optimize_and_convert_to_python(self, bf_filename, result_file_name = "test.py"):
        with open(bf_filename, 'r') as file:
             bf_code = file.read()

        self.loop_map = self.preprocess_loops(bf_code)
        optimized_python_code = self.optimize(bf_code)

        py_filename = os.path.join("out",result_file_name)
        with open(py_filename, 'w') as file:
            file.write(self.generate_python_code(optimized_python_code))
        print(f"Python code generated: {py_filename}")

    def generate_python_code(self, optimized_python_code):
        python_code_template = """import sys

def main():
    tape = [0] * 30000  # Initialize tape

    {}
    print()  # New line after program execution

if __name__ == "__main__":
    main()
        """
        # indented_code = '\n'.join('\t' + line for line in optimized_python_code.splitlines())
        indented_code = optimized_python_code.replace('\n', '\n    ')
        return python_code_template.format(indented_code)
if __name__ == "__main__":
    solver = BrainfuckSymbolicSolver()

    input_folder_path = "C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\BrainfuckPrograms"
    output_folder_path = "C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\BFTranspiledPrograms"

    files = os.listdir(input_folder_path)

    #file = "Helloworld.b"
    #solver.optimize_and_convert_to_python(os.path.join(input_folder_path, file), os.path.join(output_folder_path, os.path.splitext(file)[0] + '.py'))

    for file in files:
        input_file_name = os.path.join(input_folder_path, file)
        output_file_name = os.path.join(output_folder_path, os.path.splitext(file)[0] + '.py')

    start = time.time()
    solver.optimize_and_convert_to_python("test.b",result_file_name="ttt.py")
    end = time.time()
    print(end - start)
