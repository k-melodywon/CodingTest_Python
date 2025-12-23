a,b= map(int, input().split())
c = int(input())
min = b+c

if min >= 60:
    while (min) >= 60:
        a = a+1
        min = min - 60
    if a >= 24:
        a = a-24
    print(a,min)
        
else:
    print(a, min)
