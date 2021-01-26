# Problem
# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
# Function Description
# Complete the sockMerchant function in the editor below.
# sockMerchant has the following parameter(s):
# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns
# int: the number of pairs
# Input Format
# The first line contains an integer , the number of socks represented in . 
# The second line contains  space-separated integers, , the colors of the socks in the pile.
# Sample Input
# STDIN                       Function
# -----                       --------
# 9                           n = 9
# 10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# Sample Output
# 3

# Solution

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    total_pairs = 0
    i = 0
    colours = list(set(ar))
    if n <= 1:
        print(total_pairs)
    else:
        while i< len(colours):
            colour = colours[i]
            total_pairs = total_pairs + int(ar.count(colour) / 2)    
            i = i + 1
        print(total_pairs)
    return total_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
