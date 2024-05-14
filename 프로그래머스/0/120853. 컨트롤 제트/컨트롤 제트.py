def solution(s):
    answer = 0
    list = s.split(' ')
    for i in range(0,len(list)):
        if ( list[i] == "Z" ):
            answer = answer - int(list[i-1])
        else:
            answer += int(list[i])
            
    return answer