Problem
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
