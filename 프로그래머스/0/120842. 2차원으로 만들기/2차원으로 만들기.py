def solution(num_list, n):
    answer = []
    temp = []
    check = 0
    
    for i in num_list:
        check += 1
        temp.append(i)
        if(check == n):
            answer.append(temp)
            temp = []
            check = 0
                        
    return answer