import sys
n, m = map(int, sys.stdin.readline().split())
basket = list(range(1, n + 1))

for a in range(m):
    i, j = map(int, sys.stdin.readline().split())
    basket[i-1:j] = basket[i-1:j][::-1]

print(*basket)