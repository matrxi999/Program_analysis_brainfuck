import time
import subprocess


def get_timestamp():
    return time.time()


def get_elapsed_time(start_time, end_time):
    return end_time - start_time


def run_program_multiple_times(program, file_path, times_to_run):
    elapsed_times = []
    for _ in range(times_to_run):
        start_time = get_timestamp()
        subprocess.run(["python", program, file_path])
        end_time = get_timestamp()
        elapsed_times.append(get_elapsed_time(start_time, end_time))
    return elapsed_times


def get_avr_elapsed_time(program, file_path, times_to_run):
    elapsed_times = run_program_multiple_times(program, file_path, times_to_run)
    return sum(elapsed_times) / len(elapsed_times)
