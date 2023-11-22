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
            self.expr = self.symbol + initial_value
            self.is_changed = True

    def get_concrete_val(self):
        concrete, _ = self.expr.as_coeff_Add()
        return int(concrete)

    def reset(self):
        self.expr = self.symbol

    def sym_add(self):
        self.expr += 1

    def __add__(self, n):
        # Creating a new instance with the updated expression
        # self.is_changed = True
        return SymbolicValue(symbolic=str(self.symbol), initial_value=self.get_concrete_val() + n)

    def __sub__(self, n):
        # self.is_changed = True
        # Creating a new instance with the updated expression
        return SymbolicValue(symbolic=str(self.symbol), initial_value=self.get_concrete_val() - n)

    def sym_sub(self):
        self.expr -= 1

    def __str__(self):
        # concrete, _ = self.expr.as_coeff_Add()
        return str(self.expr)


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
            self.expr = self.symbol + initial_value
            self.is_changed = True

    def get_concrete_val(self):
        concrete, _ = self.expr.as_coeff_Add()
        return int(concrete)

    def reset(self):
        self.expr = self.symbol

    def sym_add(self):
        self.expr += 1

    def __add__(self, n):
        # Creating a new instance with the updated expression
        # self.is_changed = True
        return SymbolicValue(symbolic=str(self.symbol), initial_value=self.get_concrete_val() + n)

    def __sub__(self, n):
        # self.is_changed = True
        # Creating a new instance with the updated expression
        return SymbolicValue(symbolic=str(self.symbol), initial_value=self.get_concrete_val() - n)

    def sym_sub(self):
        self.expr -= 1

    def __str__(self):
        # concrete, _ = self.expr.as_coeff_Add()
        return str(self.expr)


class BrainfuckSymbolicSolver:
    # LATEST
    def __init__(self):
        self.tape = [0 for _ in range(3000)]  # tape of size 3000
        self.pointer = 0
        self.symbolic_state = {}  # to track the state - mixed sym and concrete
        self.loop_stack = []  # to keep track of loop
        self.last_state = []
        self.loop_map = {}

    def interpret(self, code):
        #  interpreter
        for char in code:
            self.execute_command(char)

    def get_loop_start(self, index, code):
        counter = 1  # counter to handle nested loops
        for i in range(index - 1, -1, -1):
            if code[i] == ']':
                counter += 1
            elif code[i] == '[':
                counter -= 1
                if counter == 0:
                    return i
        return -1

    def get_loop_end(self, index, code):
        counter = 1  # counter to handle nested loops
        for i in range(index + 1, len(code)):
            if code[i] == '[':
                counter += 1
            elif code[i] == ']':
                counter -= 1
                if counter == 0:
                    return i
        return -1

    def handle_loop_start(self, index, loop_end):
        if isinstance(self.tape[self.pointer], int):
            if self.tape[self.pointer] == 0:
                return loop_end  # Go to loop end
            else:
                self.loop_stack.append(self.pointer)
                return index
        return index

    def handle_loop_end(self, index, loop_start):
        if isinstance(self.tape[self.pointer], int):
            if self.tape[self.pointer] != 0:
                #self.pointer = self.loop_stack[-1]
                return loop_start
            else:
                self.loop_stack.pop()
                return index
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
        # handel loops

    def execute_loops(self, char, index, code):
        if char == '[':
            loop_end = self.loop_map[index]
            return self.handle_loop_start(index, loop_end)
        elif char == ']':
            loop_start = self.loop_map[index]
            return self.handle_loop_end(index, loop_start)

    def symbolic_add_sub(self, char):
        if self.pointer not in self.symbolic_state:
            self.symbolic_state[self.pointer] = SymbolicValue()
        if char == '+':
            self.symbolic_state[self.pointer].increment()
        elif char == '-':
            self.symbolic_state[self.pointer].decrement()

    def optimize(self, code):
        optimized_code = ""
        self.pointer = 0

        # had_to_trans = False
        index = 0
        while index < len(code):
            char = code[index]
            #print(f'Pointer = {self.pointer}, index = {index}, value = {self.tape[self.pointer]}, char = {char} ')
            if char in ['+', '-', '>', '<']:
                self.execute_command(char)
            elif char == '[':
                index = self.execute_loops(char, index, code)
            elif char == ']':
                index = self.execute_loops(char, index, code)
            elif char == '.':
                optimized_code += self.optimize_print()
                # had_to_trans = True
                optimized_code += f"print(chr(tape[{self.pointer}]), end='')\n"

            elif char == ',':
                optimized_code += f"tape[{self.pointer}] = input()\n"
                self.tape[self.pointer] = SymbolicValue()

            # else:
            # optimized_code += self.apply_optimizations()
            # optimized_code += char
            index += 1
        if code[index - 1] != '.':
            # Apply any remaining optimizations at the end if it wasnt a print as last command
            optimized_code += self.apply_optimizations()
        return optimized_code
    
    def optimize_print(self):
        optimized_code = ""
        if isinstance(self.tape[self.pointer], SymbolicValue):
            if self.tape[self.pointer].get_concrete_val() != 0:
                        optimized_code += f"tape[{self.pointer}] += {self.tape[self.pointer].get_concrete_val()}\n"
        else:
            optimized_code += f"tape[{self.pointer}] = {self.tape[self.pointer]}\n"
        return optimized_code

    def apply_optimizations(self):
        optimized_code = ""
        for pointer in range(len(self.tape)):

            if self.last_state == []:
                if self.tape[pointer] == 0:
                    continue
                if isinstance(self.tape[pointer], SymbolicValue):
                    # Is a symbolic expression
                    # optimized_code += f"tape[{pointer}] = input()\n"

                    if self.tape[pointer].get_concrete_val() != 0:
                        optimized_code += f"tape[{pointer}] += {self.tape[pointer].get_concrete_val()}\n"
                    # else:
                    #     optimized_code += f"tape[{pointer}] = input()\n"
                else:
                    # Is a concrete value
                    optimized_code += f"tape[{pointer}] = {self.tape[pointer]}\n"
                    # value.reset()
            else:
                if isinstance(self.tape[pointer], SymbolicValue) and isinstance(self.last_state[pointer],
                                                                                SymbolicValue):
                    # was and still is symbolic
                    if self.tape[pointer].get_concrete_val() != 0 and self.tape[pointer].get_concrete_val() != \
                            self.last_state[pointer].get_concrete_val():
                        optimized_code += f"tape[{pointer}] += {self.tape[pointer].get_concrete_val()}\n"
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

        self.last_state = copy.deepcopy(self.tape)
        return optimized_code

    def handle_loop(self, code):
        current_i = self.symbolic_state[self.pointer]

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
        #bf_code = bf_filename
        bf_code_striped = bf_code.strip()
        bf_code_no_new_line = bf_code.replace("\n", "")
        # print(bf_code_no_new_line)
        self.loop_map = self.preprocess_loops(bf_code_no_new_line)
        optimized_python_code = self.optimize(bf_code_no_new_line)
        # py_filename = bf_filename.rsplit('.', 1)[0] + '.py'
        py_filename = result_file_name
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

    start = time.time()
    solver.optimize_and_convert_to_python("test.b",result_file_name="ttt.py")
    end = time.time()
    print(end - start)
