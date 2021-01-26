Problem
Objective 
In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean. Check out the Tutorial tab for learning materials and an instructional video!
Task 
Given an array, , of  integers and an array, , representing the respective weights of 's elements, calculate and print the weighted mean of 's elements. Your answer should be rounded to a scale of decimal place (i.e.,  format).
Input Format
The first line contains an integer, , denoting the number of elements in arrays  and . 
The second line contains  space-separated integers describing the respective elements of array . 
The third line contains  space-separated integers describing the respective elements of array .
Output Format
Print the weighted mean on a new line. Your answer should be rounded to a scale of  decimal place (i.e.,  format).
Sample Input
5
10 40 30 50 20
1 2 3 4 5
Sample Output
32.0


Solution
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))
Z = 0

for i in range(N):
    Z = Z + (X[i]*W[i])
W_sum = sum(W)
Weight_mean = round((Z / W_sum),1)

print(Weight_mean)
