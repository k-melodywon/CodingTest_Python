def solution(n):
    gcd = 0
    
    if (n>=6):
        min = 6
    else:
        min = n
        
    for i in range(1,min+1):
        if (n%i==0)&(6%i==0):
            gcd = i;
            
    return (n*6//gcd)/6