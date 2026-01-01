
import sys
n = int(sys.stdin.readline().strip())
result = ''

for i in range(0,n):
    k, word = sys.stdin.readline().split()
    k = int(k)
    for j in word:
        result += j * k
    print(result)
    result = ''    