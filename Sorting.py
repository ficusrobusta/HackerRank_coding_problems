"""
Problem
Task 
Given an array, , of size  distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following  lines:
Array is sorted in numSwaps swaps. 
where  is the number of swaps that took place.
First Element: firstElement 
where  is the first element in the sorted array.
Last Element: lastElement 
where  is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.
Example

original a: 4 3 1 2
round 1  a: 3 1 2 4 swaps this round: 3
round 2  a: 1 2 3 4 swaps this round: 2
round 3  a: 1 2 3 4 swaps this round: 0
In the first round, the  is swapped at each of the  comparisons, ending in the last position. In the second round, the  is swapped at  of the  comparisons. Finally, in the third round, no swaps are made so the iterations stop. The output is the following:
Array is sorted in 5 swaps.
First Element: 1
Last Element: 4
Input Format
The first line contains an integer, , the number of elements in array . 
The second line contains  space-separated integers that describe .
Constraints

, where .
Output Format
Print the following three lines of output:
Array is sorted in numSwaps swaps. 
where  is the number of swaps that took place.
First Element: firstElement 
where  is the first element in the sorted array.
Last Element: lastElement 
where  is the last element in the sorted array.
Sample Input 0
3
1 2 3
Sample Output 0
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
"""

Solution
#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numSwaps += 1
        
firstElement = a[0]
lastElement = a[-1]

print("Array is sorted in", numSwaps, "swaps.")
print("First Element:", firstElement)
print("Last Element:",lastElement)
