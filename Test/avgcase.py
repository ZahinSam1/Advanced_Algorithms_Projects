import time
import random
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def measure_time(size_of_array, is_worst_case=False):
    if is_worst_case:
        array = list(range(size_of_array, 0, -1))  # Generate array in descending order
    else:
        array = [random.randint(1, size_of_array) for _ in range(size_of_array)]

    with open('average_case_array.txt', 'a') as file:
        file.seek(0, 2)
        file.write(f'size of {size_of_array}: {array}\n\n')

    start_time = time.time()
    quicksort(array)
    end_time = time.time()

    return end_time - start_time


input_size_start = 10
input_size_end = 100000
input_sizes = []

while input_size_start <= input_size_end:
    input_sizes.append(input_size_start)

    if input_size_start < 100:
        input_size_start += 10
    elif input_size_start < 1000:
        input_size_start += 100
    elif input_size_start < 10000:
        input_size_start += 1000
    else:
        input_size_start += 10000


execution_times = []
start_time_total = time.time()
for size in input_sizes:
    execution_time = measure_time(size)
    execution_times.append(execution_time)
end_time_total = time.time()

total_execution_time = end_time_total - start_time_total


# Write execution_times to a text file
with open('execution_times.txt', 'w') as file:
    for time_val, sizes in zip(execution_times, input_sizes):
        file.write(f'{sizes} = {time_val:.16f}\n')

# To measure the worst-case time complexity
worst_execution_times = []
for size in input_sizes:
    execution_time = measure_time(size, is_worst_case=True)
    worst_execution_times.append(execution_time)

# Write worst_execution_times to a text file
with open('worst_case_execution_times.txt', 'w') as file:
    for time_val, sizes in zip(worst_execution_times, input_sizes):
        file.write(f'{sizes} = {time_val:.16f}\n')

worst_total_execution_time = sum(worst_execution_times)


# Plot the results for average-case time complexity
plt.plot(input_sizes, execution_times, marker='.')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title(f'Quick Sort Time Complexity (Average Case)\nTotal Execution Time: {total_execution_time:.2f}')
plt.grid(True)
plt.show()


# # Plot the results for worst-case time complexity
# plt.plot(input_sizes, worst_execution_times, marker='.')
# plt.xlabel('Input Size')
# plt.ylabel('Execution Time (seconds)')
# plt.title(f'Quick Sort Time Complexity (Worst Case)\nTotal Execution Time: {worst_total_execution_time:.2f}')
# plt.grid(True)
# plt.show()
