import random
import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(10**6)  # Increase recursion limit

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i][2] <= pivot[2]:  # Comparing finish times
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

def activity_selection(arr):
    sorted_activities = quick_sort(arr)
    selected_activities = [sorted_activities[0]]
    prev_finish_time = sorted_activities[0][2]

    for activity in sorted_activities[1:]:
        if activity[1] >= prev_finish_time:
            selected_activities.append(activity)
            prev_finish_time = activity[2]

    return selected_activities

def generate_random_activity_list(size):
    activity_prefix = "activity"
    activity_list = []

    for i in range(1, size+1):
        activity_name = f"{activity_prefix} {i}"
        start_time = random.randint(0, 100)
        finish_time = random.randint(start_time, start_time+100)
        activity = (activity_name, start_time, finish_time)
        activity_list.append(activity)

    return activity_list

# Generate random activity list
activity_list = generate_random_activity_list(10000)
print("Original Activity List:")
for activity in activity_list:
    print(activity)

# Measure execution time
start_time = time.time()

# Quick sort
sorted_activities = quick_sort(activity_list)
print("\nSorted Activity List (Based on Finish Time):")
for activity in sorted_activities:
    print(activity)

# Activity selection
selected_activities = activity_selection(sorted_activities)

end_time = time.time()

execution_time = end_time - start_time
print("\nTotal Execution Time:", execution_time, "seconds")


with open("time_data.txt", "w") as file:
    file.write(f"Original Time: {execution_time}\n")
    file.write("Sorted Time:\n")
    for activity in selected_activities:
        file.write(str(activity) + "\n")

# Plot time complexity graph
# sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 250000, 500000, 750000, 1000000]



input_size_start = 10   #just a minimum size to start off the experiment
input_size_end = 10000  #the maximum size to end

input_sizes = [] #to store all the size value of the input data

#loop to create the array of input data size
while input_size_start <= input_size_end:
    
    input_sizes.append(input_size_start) #keep appending the input data size
    
    if input_size_start < 100:
        input_size_start += 10  #if size is less than 100 then add 10 with every iteration
    elif input_size_start < 1000:
        input_size_start += 100 #if size is less than 1000 then add 100 with every iteration
    elif input_size_start < 10000:
        input_size_start += 100 #if size is less than 10000 then add 1000 with every iteration
    else:
        input_size_start += 1000 #if more than 10K then increase by 10K with every iteration

times = []

for size in input_sizes:
    total_time = 0.0
    iterations = 50  # Increase number of iterations
    
    for _ in range(iterations):
        activity_list = generate_random_activity_list(size)
        start_time = time.time()
        # Quick sort
        sorted_activities = quick_sort(activity_list)
        # Activity selection
        selected_activities = activity_selection(sorted_activities)

        end_time = time.time()
        execution_time = end_time - start_time
        total_time += execution_time

    average_time = total_time / iterations
    times.append(average_time)

plt.plot(input_sizes, times, marker='.')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Time Complexity Graph For Activity Selection Problem')
plt.grid(True)
plt.show()
