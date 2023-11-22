import os
from performance_evaluator import get_avr_elapsed_time


def get_program_files(folder_path):
    return [file for file in os.listdir(folder_path)]


def test_brainfuck_files(programs_folder, times_to_run):
    brainfuck_files = get_program_files(programs_folder)
    results = {}
    for file in brainfuck_files:
        file_path = os.path.join(programs_folder, file)
        avg_time = get_avr_elapsed_time(file_path, times_to_run)
        results[file] = avg_time
    return results
