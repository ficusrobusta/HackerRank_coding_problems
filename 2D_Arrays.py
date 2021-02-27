"""
Problem
Objective 
Today, we are building on our knowledge of arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video.
Context 
Given a  2D Array, :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:
a b c
  d
e f g
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.
Task 
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
Example
In the array shown above, the maximum hourglass sum is  for the hourglass in the top left corner.
Input Format
There are  lines of input, where each line contains  space-separated integers that describe the 2D Array .
Constraints


Output Format
Print the maximum hourglass sum in .
Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output
19

"""
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))



numrows = len(arr)    
numcols = len(arr[0])
hourglass = []
i = 0
j = 0
while i in range(numrows-2):
    while j in range(numcols-2):
        hourglass = hourglass + [int(arr[i][j]) + int(arr[i][j+1]) + int(arr[i][j+2]) + int(arr[i+1][j+1]) + int(arr[i+2][j]) + int(arr[i+2][j+1]) + int(arr[i+2][j+2])]
        j= j + 1
    else:
        i=i+1
        j=0
    continue
A = max(hourglass)
print(A)




