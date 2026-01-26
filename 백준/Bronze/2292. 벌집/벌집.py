import sys
k = int(sys.stdin.readline().strip())
if k == 1 :
    print(1)
else:
    n=1
    count = 2
    sum = 3*n**2+3*n+1
    
    while sum < k:
        count += 1
        n += 1
        sum = 3*n**2+3*n+1
        
    print(count)