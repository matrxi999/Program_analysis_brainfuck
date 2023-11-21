from sympy import Symbol, simplify


class SymbolicValue:
    def __init__(self, initial_value=None, symbolic=False):
        self.symbolic = symbolic
        if symbolic:
            self.value = Symbol('x')
        else:
            self.value = initial_value if initial_value is not None else 0

    def increment(self):
        self.value += 1
        if self.symbolic:
            self.value = simplify(self.value)

    def decrement(self):
        self.value -= 1
        if self.symbolic:
            self.value = simplify(self.value)

    def is_changed(self):
        return self.value != 0 or self.symbolic

    def get_optimized_value(self):
        return simplify(self.value) if self.symbolic else self.value

    def reset(self):
        self.value = 0

    def __str__(self):
        return str(self.value)


class BrainfuckSymbolicSolver:
    def __init__(self):
        self.tape = [SymbolicValue() for _ in range(30000)]
        self.pointer = 0
        self.symbolic_state = {}  # to track symbolic values
        self.loop_stack = []  # to keep track of loop

    def interpret(self, code):
        # sym interpret
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
        if self.symbolic_state[self.pointer].get_optimized_value() == 0:
            return loop_end  # Go to loop end
        else:
            self.loop_stack.append(self.pointer)
            return index

    def handle_loop_end(self, index, loop_start):
        if self.symbolic_state[self.pointer].get_optimized_value() != 0:
            self.pointer = self.loop_stack[-1]
            return loop_start
        else:
            self.loop_stack.pop()
            return index

    def execute_command(self, char):
        # Execute a single Brainfuck command
        if char == '>':
            self.pointer += 1
        elif char == '<':
            self.pointer -= 1
        elif char in ['+', '-']:
            self.symbolic_add_sub(char)

    def execute_loops(self, char, index, code):
        if char == '[':
            loop_end = self.get_loop_end(index, code)
            return self.handle_loop_start(index, loop_end)
        elif char == ']':
            loop_start = self.get_loop_start(index, code)
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
        self.symbolic_state = {}

        index = 0
        while index < len(code):
            char = code[index]
            if char in ['+', '-', '>', '<']:
                self.execute_command(char)
            elif char == '[':
                index = self.execute_loops(char, index, code)
            elif char == ']':
                index = self.execute_loops(char, index, code)
            elif char == '.':
                # optimized_code += self.apply_optimizations()
                optimized_code += f"print(chr(tape[{self.pointer}]), end='')\n"
            # else:
            # optimized_code += self.apply_optimizations()
            # optimized_code += char

            index += 1

        optimized_code += self.apply_optimizations()
        return optimized_code

    def apply_optimizations(self):
        optimized_code = ""
        for pointer, symbolic_value in self.symbolic_state.items():
            # if symbolic_value.is_changed():
            self.tape[pointer] = symbolic_value
            optimized_code += f"tape[{pointer}] = {symbolic_value.get_optimized_value()}\n"
            # value.reset()

        # self.symbolic_state = {}
        return optimized_code

    def apply_loop_optimizations(self):
        return "[]\n"  # Placeholder for actual loop optimization logic

    def optimize_and_convert_to_python(self, bf_filename):
        # with open(bf_filename, 'r') as file:
        #     bf_code = file.read()
        bf_code = bf_filename
        optimized_python_code = self.optimize(bf_code)
        # py_filename = bf_filename.rsplit('.', 1)[0] + '.py'
        py_filename = "test.py"
        with open(py_filename, 'w') as file:
            file.write(self.generate_python_code(optimized_python_code))

        print(f"Python code generated: {py_filename}")

    def generate_python_code(self, optimized_python_code):
        python_code_template = """import sys

def main():
    tape = [0] * 30000  # Initialize tape
    pointer = 0

    {}
    print()  # New line after program execution

if __name__ == "__main__":
    main()
        """
        # indented_code = '\n'.join('\t' + line for line in optimized_python_code.splitlines())
        indented_code = optimized_python_code.replace('\n', '\n    ')
        return python_code_template.format(indented_code)


if __name__ == "__main__":
    # solver = BrainfuckSymbolicSolver()
    # solver.interpret("++>+-")
    # solver.optimize()

    solver = BrainfuckSymbolicSolver()
    solver.optimize_and_convert_to_python("+++++.>+.<[->[-]<]+")
    # print("Optimized python code:", solver.optimize_and_convert_to_python("+.++--"))

    # solver = BrainfuckSymbolicSolver()
    # optimized_code = solver.optimize("+++++>+++")
    # print("Optimized code:", optimized_code)

    # optimized_code = solver.optimize("++>+-")
    # print("Optimized code:", optimized_code)
