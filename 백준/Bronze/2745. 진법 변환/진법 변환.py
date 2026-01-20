import sys
n , b= sys.stdin.readline().split()
total = 0
j = 0
for i in reversed(n):
    if '0' <= i <= '9':
        a = int(i)
    else:
        a = ord(i)-55
    total += a*((int(b))**j)
    j += 1
print(total)