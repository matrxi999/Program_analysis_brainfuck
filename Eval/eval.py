from batch_performance_brainfuck_tester import test_brainfuck_files
from stats_eval_results import students_t_test, transform_to_log
from visualize_performance_results import plot_comparison
import json
def save_results(file_path, results):
    with open(file_path, 'w') as file:
        json.dump(results, file)
def load_results(file_path):
    with open(file_path, 'r') as file:
        data_dict = json.load(file)
        return data_dict


if __name__ == "__main__":

    times_to_run = 1

    unoptimized_folder = "C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\ASTtranspiler\\TranspiledBFfilesNonOptimized"
    syntactic_folder = "C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\ASTtranspiler\\TranspiledBFfiles"
    symbolic_folder = "C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\Symbolic\\TranspiledBFfiles"

    unoptimized_results = test_brainfuck_files(unoptimized_folder, times_to_run)
    syntactic_results = test_brainfuck_files(syntactic_folder, times_to_run)
    symbolic_results = test_brainfuck_files(symbolic_folder, times_to_run)

    save_results("C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\Eval\\results\\unoptimized_results.json", unoptimized_results)
    save_results("C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\Eval\\results\\syntactic_results.json", syntactic_results)
    save_results("C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\Eval\\results\\symbolic_results.json", symbolic_results)

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
