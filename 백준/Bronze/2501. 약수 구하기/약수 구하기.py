import sys
a, b= map(int, sys.stdin.readline().split())
G = []

for i in range(1,a+1):
    if a%i == 0:
        G.append(i)
try:
    print(G[b-1])
except:
    print(0)