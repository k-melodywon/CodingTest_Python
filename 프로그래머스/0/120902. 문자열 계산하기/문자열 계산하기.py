def solution(my_string):
    answer = 0
    list = my_string.split()
    answer = int(list[0])
    for i in range(0,len(list)):
        if (i%2==1 and list[i]=='+'):
            answer += int(list[i+1])
        elif (i%2==1 and list[i]=='-'):
            answer -= int(list[i+1])
            
    return answer