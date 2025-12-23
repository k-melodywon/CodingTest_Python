import sys
a, b = 1,1
while a != None and b != None:
    try:
        a,b = map(int, sys.stdin.readline().split()) 
        print(a+b)
    except ValueError:
        break