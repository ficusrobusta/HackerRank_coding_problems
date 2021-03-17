"""
Problem
There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first letters of the infinite string.
Example 
 

The substring we consider is , the first  characters of the infinite string. There are  occurrences of a in the substring.
Function Description
Complete the repeatedString function in the editor below.
repeatedString has the following parameter(s):
s: a string to repeat
n: the number of characters to consider
Returns
int: the frequency of a in the substring
Input Format
The first line contains a single string, . 
The second line contains an integer, .
Constraints


For  of the test cases, .
Sample Input
Sample Input 0
aba
10
Sample Output 0
7
""
#Solution
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s) >= n:
        num_a = s.count("a",0,n)
        
    else:
        factor = int(n / len(s))
        remainder = n % len(s)
        if remainder == 0:
            num_a = s.count("a") * factor
            
        else:
            num_a = (s.count("a") * factor) + s.count("a",0,remainder)
    print(num_a)
    return num_a
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
