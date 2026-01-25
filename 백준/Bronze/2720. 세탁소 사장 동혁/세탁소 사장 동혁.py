import sys
k = int(sys.stdin.readline().strip())
q, d, n, p = 0,0,0,0
for i in range(k):
    c = int(sys.stdin.readline().strip())

    q = c//25
    c = c%25

    d = c//10
    c = c%10

    n = c//5
    c = c%5

    p = c//1
    print(q, d, n, p)
