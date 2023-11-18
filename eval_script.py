import subprocess
import time

def run_python_file(file_name, times):
    times_run = []

    for _ in range(times):
        start_time = time.time()
        subprocess.run(["python", file_name])
        end_time = time.time()

        execution_time = end_time - start_time
        times_run.append(execution_time)

    return times_run

# Example usage
file_to_run = "your_script.py"  # Replace with your Python file name
number_of_runs = 5  # Number of times to run the file

run_times = run_python_file(file_to_run, number_of_runs)
for i, run_time in enumerate(run_times, 1):
    print(f"Run {i}: {run_time} seconds")
    if i == 10:
        break

# To calculate and print average run time
average_time = sum(run_times) / len(run_times)
print(f"Average run time: {average_time} seconds")
