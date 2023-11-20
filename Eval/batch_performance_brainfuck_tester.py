import os
from performance_evaluator import get_avr_elapsed_time


def get_brainfuck_files(folder_path):
    return [file for file in os.listdir(folder_path)]


def test_brainfuck_files(folder_path, program, times_to_run):
    brainfuck_files = get_brainfuck_files(folder_path)
    results = {}
    for file in brainfuck_files:
        file_path = os.path.join(folder_path, file)
        avg_time = get_avr_elapsed_time(program, file_path, times_to_run)
        results[file] = avg_time
    return results
