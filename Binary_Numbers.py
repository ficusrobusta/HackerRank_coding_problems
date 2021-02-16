# Problem
# Task 
# Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. When working with different bases, it is common to show the base as a subscript.
# Example 

# The binary representation of  is . In base , there are  and  consecutive ones in two groups. Print the maximum, .
# Input Format
# A single integer, .
# Constraints

# Output Format
# Print a single base- integer that denotes the maximum number of consecutive 's in the binary representation of .
# Sample Input 1
# 5
# Sample Output 1
# 1
# Sample Input 2
# 13
# Sample Output 2
# 2

# Solution 

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

binary = []
remainder = []

while n > 0:
    if n == 1:
        remainder = 1
    else:
        remainder = n % 2
        
    n = int(n / 2)
    binary = [remainder] + binary
    
ones = []
count = []


first = binary.index(1)
count = 1
i = 1
while first + i < len(binary):
    if binary[first + i] == 1:
        count = count + 1
        i = i + 1
    else:
        ones = ones + [count]
        count = 0
        i = i + 1
    
print(max(ones))
