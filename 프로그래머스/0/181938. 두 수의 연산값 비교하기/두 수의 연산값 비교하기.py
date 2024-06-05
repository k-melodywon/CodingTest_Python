def solution(a, b):
    answer = 2*a*b
    temp = str(a)+ str(b)
    
    if (int(temp)>= 2*a*b):
        answer = int(temp)
    return answer