import sys
num = []
for i in range(9):
    num.append(int(sys.stdin.readline().strip()))


big = max(num)

print(big , num.index(big)+1)