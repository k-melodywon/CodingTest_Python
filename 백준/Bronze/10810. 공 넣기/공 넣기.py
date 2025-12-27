import sys
n, m = map(int, sys.stdin.readline().split())
basket = n*[0]
for a in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for b in range(i-1,j):
        basket[b] = k

for a in basket:
    print(a)   