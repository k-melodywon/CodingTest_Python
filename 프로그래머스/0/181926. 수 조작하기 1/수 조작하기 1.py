def count(control):
    if(control=='w'):
        return 1
    elif(control == 's'):
        return -1
    elif(control == 'd'):
        return 10
    elif(control == 'a'):
        return -10
    

def solution(n, control):
    answer = n
    for i in control:
        answer += count(i)
    return answer