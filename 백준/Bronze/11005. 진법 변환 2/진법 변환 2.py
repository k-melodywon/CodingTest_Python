
import sys
n , b= map(int, sys.stdin.readline().split())
total = ''
while n > 0 :
    if n%b < 10:
        total += str(n%b)
    else:
        total += chr((n%b)+55)
    n = n//b
print(total[::-1])