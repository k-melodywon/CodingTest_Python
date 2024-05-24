def solution(my_str, n):
    answer = []
    temp = ''
    count = 0
    for i in my_str:
        if(count<n):
            temp = temp + i
            count += 1
        else:
            answer.append(temp)
            count = 1
            temp = i
    answer.append(temp)
    return answer