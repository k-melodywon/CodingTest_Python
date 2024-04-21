def solution(number1, denom1, number2, denom2):
    a = number1*denom2+number2*denom1
    b = denom1*denom2
    min = 0
    gcd = 0
    
    if (a>=b):
        min = b
    else:
        min = a
        
    for i in range(1,min+1):
        if (a%i==0)&(b%i==0):
            gcd = i;
    
    
    answer = [a//gcd, b//gcd]
    
    return answer