import sys
a = int(sys.stdin.readline().strip())
n=1
s = 2*n**2-n
while s < a:
    n += 1
    s = 2*n**2-n
d = 2*n-1
num = 2*(n-1)**2-(n-1)
A1 = [i for i in range(1,d+1)]
A2 = [i for i in range(d-1,0,-1)]
A = A1+A2
remain = a-num-1

n2=1
s2 = 2*n2**2+n2
while s2 < a:
    n2 += 1
    s2 = 2*n2**2+n2
d = 2*n2
num2 = 2*(n2-1)**2+(n2-1)
B1 = [i for i in range(1,d+1)]
B2 = [i for i in range(d-1,0,-1)]
B = B1+B2
remain2 = a-num2-1
print(f"{A[remain]}/{B[remain2]}")
