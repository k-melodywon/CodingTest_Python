import sys
answer = [1,1,2,2,2,8]
a = list(map(int, sys.stdin.readline().split()))
for i in range(0,6):
    answer[i] = answer[i] - a[i]
    print(answer[i])