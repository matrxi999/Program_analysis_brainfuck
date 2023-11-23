## Installation

To set up the environment for this project, you need to install the dependencies listed in `requirements.txt`. You can do this by running the command in your terminal:

`pip install -r requirements.txt`

## Usage

### Symbolic Analyzer

The symbolic analyzer is found in `symbolic_solver_partial_exec.py`. 

To run the symbolic analyzer (that optimizes and transpiles), you can use the command:

`solver.optimize_and_convert_to_python(input_file_path, output_file_path)`

Replace `input_file_path` with the path of your input file and `output_file_path` with the desired path for your output file.

### Syntactic Analyzer

The syntactic analyzer is found in `ASTtranspiler.py`. It can be executed using the following command:

`optimized_python_code = translate_from_ast(generate_AST(input_file_path),
optimize_arithmetic=True, optimize_pointer=True,
optimize_consecutive_loops=True, optimize_clear_loops=True,
delete_first_loop=True, remove_redundant_sequences=True,
copy_loop_optimization=True)`


This will perform an optimized translation of your code. Replace `input_file_path` with the path of your input file.

### Non-optimized transpiler
If you prefer a non-optimized translation, set all the boolean values to false:

`optimized_python_code = translate_from_ast(generate_AST(input_file_path),
optimize_arithmetic=False, optimize_pointer=False,
optimize_consecutive_loops=False, optimize_clear_loops=False,
delete_first_loop=False, remove_redundant_sequences=False,
copy_loop_optimization=False)`

By adjusting the boolean values you can customize the level of optimization that is to be applied during the translation process.
