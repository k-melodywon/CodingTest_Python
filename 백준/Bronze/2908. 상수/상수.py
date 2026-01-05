import sys
a, b = sys.stdin.readline().split()
a = int(''.join(reversed(a)))
b = int(''.join(reversed(b)))
answer = a
if b>a:
    answer = b
print(answer)