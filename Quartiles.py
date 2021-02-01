#Problem
# Objective 
# In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!
# Task 
# Given an array, , of  integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and  are integers.
# Input Format
# The first line contains an integer, , denoting the number of elements in the array. 
# The second line contains  space-separated integers describing the array's elements.
# Constraints

# , where  is the  element of the array.
# Output Format
# Print  lines of output in the following order:
# The first line should be the value of .
# The second line should be the value of .
# The third line should be the value of .
# Sample Input
# 9
# 3 7 8 5 12 14 21 13 18
# Sample Output
# 6
# 12
# 16

#Solution
# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median

N = int(input())
X = list(map(int, input().split()))
X = sorted(X)

if N % 2 != 0:
    L = X[:int(N/2)]
    U = X[int((N/2)+1):]
    
else:
    L = X[:int(N/2)]
    U = X[int(N/2):]

Q2 = int(median(X))
Q1 = int(median(L))
Q3 = int(median(U))

print(Q1)
print(Q2)
print(Q3)
