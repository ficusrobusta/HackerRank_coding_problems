# Solution
# Objective 
# In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.
# Task 
# The interquartile range of an array is the difference between its first () and third () quartiles (i.e., ).
# Given an array, , of  integers and an array, , representing the respective frequencies of 's elements, construct a data set, , where each  occurs at frequency . Then calculate and print 's interquartile range, rounded to a scale of  decimal place (i.e.,  format).
# Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.
# Input Format
# The first line contains an integer, , denoting the number of elements in arrays  and . 
# The second line contains  space-separated integers describing the respective elements of array . 
# The third line contains  space-separated integers describing the respective elements of array .
# Constraints

# , where  is the  element of array .
# , where  is the  element of array .
# The number of elements in  is equal to .
# Output Format
# Print the interquartile range for the expanded data set on a new line. Round your answer to a scale of  decimal place (i.e.,  format).
# Sample Input
# 6
# 6 12 8 10 20 16
# 5 4 3 2 1 5
# Sample Output
# 9.0

# Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median
N = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))
S = []

for i in range(N):
    S += [X[i]] * F[i]

S = sorted(S)
nums = len(S)

if nums % 2 != 0:
    L = S[:int(nums/2)]
    U = S[int((nums/2)+1):]
    
else:
    L = S[:int(nums/2)]
    U = S[int(nums/2):]

Q1 = median(L)
Q3 = median(U)
IQR = float(Q3 - Q1)
print(IQR)
