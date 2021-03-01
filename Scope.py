"""
Objective 
Today we're discussing scope. Check out the Tutorial tab for learning materials and an instructional video!
The absolute difference between two integers, and , is written as . The maximum absolute difference between two integers in a set of positive integers, , is the largest absolute difference between any two integers in .
The Difference class is started for you in the editor. It has a private integer array () for storing  non-negative integers, and a public integer () for storing the maximum absolute difference.
Task 
Complete the Difference class by writing the following:
A class constructor that takes an array of integers as a parameter and saves it to the  instance variable.
A computeDifference method that finds the maximum absolute difference between any numbers in  and stores it in the  instance variable.
Input Format
You are not responsible for reading any input from stdin. The locked Solution class in the editor reads in  lines of input. The first line contains , the size of the elements array. The second line has space-separated integers that describe the  array.
Constraints

, where 
Output Format
You are not responsible for printing any output; the Solution class will print the value of the  instance variable.
Sample Input
STDIN   Function
-----   --------
3       __elements[] size N = 3
1 2 5   __elements = [1, 2, 5]
Sample Output
4
"""

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = (max(self.__elements)) - (min(self.__elements))

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
