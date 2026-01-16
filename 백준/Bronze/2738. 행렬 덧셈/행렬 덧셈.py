import sys
n, m =map(int, sys.stdin.readline().split())
A = []
B = []
total = []
temp = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    B.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    for j in range(m):
        temp.append(A[i][j]+B[i][j])
    print(*temp)
    temp = []