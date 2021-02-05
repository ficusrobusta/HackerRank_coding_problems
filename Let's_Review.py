Problem
Objective 
Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the Tutorial tab for learning materials and an instructional video.
Task 
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).
Note:  is considered to be an even index.
Example

Print abc def
Input Format
The first line contains an integer,  (the number of test cases). 
Each line  of the  subsequent lines contain a string, .
Constraints


Output Format
For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.
Sample Input
2
Hacker
Rank
Sample Output
Hce akr
Rn ak

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
s = [] 

for i in range(1,T+1):
    s.append(input())

for i in s:
    print(i[::2], i[1::2])
