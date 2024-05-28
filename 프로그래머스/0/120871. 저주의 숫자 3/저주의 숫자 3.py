def is_three(a):
    answer = False
    for i in str(a):
        if (i == '3'):
            answer = True
            
    return answer
    
def solution(n):
    answer = 0
    a = 0
    list = []
    while(len(list) < n):
        a += 1
        if (a%3 != 0 and is_three(a) == False):
            list.append(a)
            
    return list[-1]