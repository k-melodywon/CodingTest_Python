import sys
a= int(sys.stdin.readline().strip())
total = [int(sys.stdin.readline().strip()) for _ in range(a)]
total.sort()
for i in total:
    print(i)