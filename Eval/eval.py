from batch_performance_brainfuck_tester import test_brainfuck_files
from stats_eval_results import t_test, normality_test, transform_to_log
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

    times_to_run = 10
    load_data = 1

    if load_data:
        unoptimized_results = load_results(
            "C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\Eval\\results\\unoptimized_results10.json")
        syntactic_results = load_results(
            "C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\Eval\\results\\syntactic_results10.json")
        symbolic_results = load_results(
            "C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\Eval\\results\\symbolic_results10.json")
    else:
        unoptimized_folder = ("C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\ASTtranspiler"
                              "\\TranspiledBFfilesNonOptimized")
        syntactic_folder = ("C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\ASTtranspiler"
                            "\\TranspiledBFfiles")
        symbolic_folder = "C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\Symbolic\\TranspiledBFfiles"

        unoptimized_results = test_brainfuck_files(unoptimized_folder, times_to_run)
        syntactic_results = test_brainfuck_files(syntactic_folder, times_to_run)
        symbolic_results = test_brainfuck_files(symbolic_folder, times_to_run)

        save_results("C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\Eval\\unoptimized_results10.json",
                     unoptimized_results)
        save_results("C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\Eval\\syntactic_results10.json",
                     syntactic_results)
        save_results("C:\\Users\\Trippy\\PycharmProjects\\Program_analysis_brainfuck\\Eval\\symbolic_results10.json",
                     symbolic_results)

    # Visualization
    plot_comparison(unoptimized_results, syntactic_results, symbolic_results)

    # Log transform data
    log_syntactic = transform_to_log(syntactic_results)
    log_symbolic = transform_to_log(symbolic_results)

    # Test normality assumption
    stat_sym, p_sym, stat_syn, p_syn = normality_test(log_symbolic, log_syntactic)

    print("Shapiro-Wilk Test Results:")
    print(f"Symbolic: {stat_sym}, p-value: {p_sym}")
    print(f"Syntactic: {stat_syn}, p-value: {p_syn}")

    # t-test
    t_stat, p_value = t_test(log_symbolic, log_syntactic)

    print("t-test Results:")
    print(f"t-stat = {t_stat} and p-value = {p_value / 2}")
