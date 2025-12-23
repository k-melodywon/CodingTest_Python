a,b= map(int, input().split())

if b >= 45:
    print(str(a)+' '+str(b-45))
else:
    if a==0:
        a = 23
    else:
        a = a-1
    print(str(a)+' '+str(b+15))