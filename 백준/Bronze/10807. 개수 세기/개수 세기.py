import sys
n = sys.stdin.readline()
num = list(map(int, sys.stdin.readline().split()))
f = int(sys.stdin.readline())
print(num.count(f))
