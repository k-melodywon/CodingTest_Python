import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    a = sys.stdin.readline().strip()
    print(a[0]+a[-1])