import sys
n , f= map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
small = []
for i in num:
    if i < f:
        print(i)