from batch_performance_brainfuck_tester import test_brainfuck_files
from stats_eval_results import students_t_test, transform_to_log
from visualize_performance_results import plot_comparison

if __name__ == "__main__":
    '''
    times_to_run = 1000
    brainfuck_files_folder = "path/to/brainfuck_folder"

    unoptimized_runner = "path/to/unoptimized_transpiler"
    syntactic_runner = "path/to/syntacticoptimized_transpiler"
    symbolic_runner = "path/to/symbolicoptimized_transpiler"

    unoptimized_results = test_brainfuck_files(brainfuck_files_folder, unoptimized_runner, times_to_run)
    syntactic_results = test_brainfuck_files(brainfuck_files_folder, syntactic_runner, times_to_run)
    symbolic_results = test_brainfuck_files(brainfuck_files_folder, symbolic_runner, times_to_run)
    '''

    unoptimized_results = {
        'file1': 1.0,
        'file2': 1.2,
        'file3': 1.2,
        'file4': 1.2,
        'file5': 0.8
    }

    syntactic_results = {
        'file1': 0.8,
        'file2': 0.9,
        'file3': 0.4,
        'file4': 0.9,
        'file5': 0.6
    }

    symbolic_results = {
        'file1': 0.7,
        'file2': 0.85,
        'file3': 0.85,
        'file4': 0.85,
        'file5': 0.5
    }

    # Student-t-test assuming log-normal distribution
    log_unoptimized = transform_to_log(unoptimized_results)
    log_syntactic = transform_to_log(syntactic_results)
    log_symbolic = transform_to_log(symbolic_results)

    t_stat_syntactic, p_syntactic = students_t_test(log_unoptimized, log_syntactic)
    t_stat_symbolic, p_symbolic = students_t_test(log_unoptimized, log_symbolic)

    print(f"Syntactic Optimization: t-stat = {t_stat_syntactic} and p-value = {p_syntactic}")
    print(f"Symbolic Optimization: t-stat= {t_stat_symbolic} and p-value = {p_symbolic}")

    # Visualization
    plot_comparison(unoptimized_results, syntactic_results, symbolic_results)
