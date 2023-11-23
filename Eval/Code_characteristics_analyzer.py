
def get_code_characteristics(brainfuck_code):
    total_loops = 0
    total_nested_loops = 0
    max_nesting_level = 0
    current_nesting_level = 0
    number_of_characters = len(brainfuck_code)

    for char in brainfuck_code:
        if char == '[':
            total_loops += 1
            current_nesting_level += 1
            if current_nesting_level > 1:
                total_nested_loops += 1
            max_nesting_level = max(max_nesting_level, current_nesting_level)
        elif char == ']':
            current_nesting_level -= 1

    return total_loops, total_nested_loops, max_nesting_level, number_of_characters

if __name__ == "__main__":
    bf_filename = "C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\brainfuckPrograms\\mandelbrot.b"

    with open(bf_filename, 'r') as file:
        brainfuck_code = file.read()

    brainfuck_code = brainfuck_code.strip().replace("\n", "")

    total_loops, total_nested_loops, max_nesting_level, number_of_characters = get_code_characteristics(brainfuck_code)
    print \
        (f"No. of characters = {number_of_characters}, Total loops = {total_loops}, Total nested loops = {total_nested_loops}, "
          f"max nesting level = {max_nesting_level}")
