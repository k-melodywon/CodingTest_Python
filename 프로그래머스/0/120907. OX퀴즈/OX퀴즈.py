def solution(quiz):
    answer = []
    for i in quiz:
        list = i.split()
        a = int(list[0])
        b = int(list[2])
        c = int(list[4])
        if(list[1]=='+'):
            if(a+b == c):
                answer.append('O')
            else:
                answer.append('X')        
        elif(list[1]=='-'):
            if(a-b == c):
                answer.append('O')
            else:
                answer.append('X') 
        list = []
    return answer