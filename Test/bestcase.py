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


def measure_time(size_of_array):
    array = [random.randint(1, size_of_array) for _ in range(size_of_array)]


    with open('average_case_array.txt', 'a') as file: #opening the file in append mode
        file.seek(0, 2) #move the file pointer to the end 
        file.write(f'size of {size_of_array} : {array} \n\n') #writing or appending to the last pointer of the file
    
    start_time = time.time()
    quicksort(array)
    end_time = time.time()

    return end_time - start_time

input_size_start = 10   #just a minimum size to start off the experiment
input_size_end = 100000 #the maximum size to end

input_sizes = [] #to store all the size value of the input data

#loop to create the array of input data size
while input_size_start <= input_size_end:
    
    input_sizes.append(input_size_start) #keep appending the input data size
    
    if input_size_start < 100:
        input_size_start += 10  #if size is less than 100 then add 10 with every iteration
    elif input_size_start < 1000:
        input_size_start += 100 #if size is less than 1000 then add 100 with every iteration
    elif input_size_start < 10000:
        input_size_start += 1000 #if size is less than 10000 then add 1000 with every iteration
    else:
        input_size_start += 10000 #if more than 10K then increase by 10K with every iteration
    
    

# Measure the execution time for each input size
execution_times = []  #array to store all the execution times after every sort

start_time_total = time.time()
for size in input_sizes:
    execution_time = measure_time(size) #get the execution time from the measure_time function
    execution_times.append(execution_time) #keep appending the execution times 

end_time_total = time.time()


# Write execution_times to a text file
with open('execution_times.txt', 'w') as file:
    for time, sizes in zip(execution_times, input_sizes):
        file.write(str(f'{sizes} = {time:.16f}') + '\n')  #writes up to 16 digits of float value in the text file

# To calculate the entire execution time
total_execution_time = end_time_total - start_time_total


# Plot the results using mat plot library
#            x-axis       y-axis         marking_points
plt.plot(input_sizes, execution_times, marker='.')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title(f'Quick Sort Time Complexity: \n total execution time {total_execution_time:.2f}')
plt.grid(True)
# plt.show()