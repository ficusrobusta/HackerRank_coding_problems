# Problem
# Objective 
# In this challenge, we practice calculating the mean, median, and mode. Check out the Tutorial tab for learning materials and an instructional video!
# Task 
# Given an array, , of  integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.
# Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of  decimal place (i.e., ,  format).
# The mean is . 
# The median is . 
# The mode is  because  occurs most frequently.
# Input Format
# The first line contains an integer, , the number of elements in the array. 
# The second line contains  space-separated integers that describe the array's elements
# , where  is the  element of the array.
# Output Format
# Print  lines of output in the following order:
# Print the mean on the first line to a scale of  decimal place (i.e., , ).
# Print the median on a new line, to a scale of  decimal place (i.e., , ).
# Print the mode on a new line. If more than one such value exists, print the numerically smallest one.
# Sample Input
# 10
# 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
# Sample Output
# 43900.6
# 44627.5
# 4978

# Solution 
# Enter your code here. Read input from STDIN. Print output to STDOUT

# from datetime import datetime
# start_time = datetime.now()

# import statistics

N = int(input())
X = list(map(int, input().split()))

x_sort = sorted(X)
mean = sum(X) / N
nums = list(set(X))
num_count = {} 
for num in nums:
    num_count[num] = X.count(num)
# num_count = sorted(num_count.items(), key=lambda x: x[1])    
if N % 2 != 0:
    median = x_sort[int(N/2)+1]
else:
    median = (x_sort[int(N/2)-1] + x_sort[int(N/2)]) / 2
# median = statistics.median(X)
all_values = num_count.values()
max_value = max(all_values)
if max_value != 1:
    # mode = statistics.mode(x_sort)
    mode = max(list(set(x_sort)), key = x_sort.count)
     
#     # mode = max(num_count, key = num_count.get)
else:
    mode = x_sort[0]
    
print(round(mean,1))
print(float(median))
print(mode)

# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))
