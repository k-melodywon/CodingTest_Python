def solution(n):
    answer = []
    temp = []
    for i in range(1,n+1):
        if (n%i == 0):
            answer.append(i)
            
    answer.remove(1)
    
    for i in answer:
        for j in answer:
            if (i%j == 0 and i!=j):
                temp.append(i)
                
    for i in temp:
        if i in answer:
            answer.remove(i)
    
    return answer