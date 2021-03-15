"""
Objective 
Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the Tutorial tab for a video on testing.
Task 
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:
If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
Example 
 returned date 
 due date
The book is returned on time, so no fine is applied.
 returned date 
 due date
The book is returned in the following year, so the fine is a fixed 10000.
Input Format
The first line contains  space-separated integers denoting the respective , , and  on which the book was actually returned. 
The second line contains  space-separated integers denoting the respective , , and  on which the book was expected to be returned (due date).
Constraints




Output Format
Print a single integer denoting the library fine for the book received as input.
Sample Input
STDIN       Function
-----       --------
9 6 2015    day = 9, month = 6, year = 2015 (date returned)
6 6 2015    day = 6, month = 6, year = 2015 (date due)
Sample Output
45
"""
# Solution
rd, rm, ry = [int(x) for x in input().split(' ')]
ed, em, ey = [int(x) for x in input().split(' ')]

if ry < ey:
    print(0)
elif ry > ey:
    print (10000)
elif rm > em:
    print ((rm-em)*500)
elif rd > ed:
    print((rd-ed)*15)
else:
    print(0)
    
