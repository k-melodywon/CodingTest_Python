def solution(my_string, num1, num2):
    answer = list(my_string)
    temp = ''
    temp = answer[num1]
    answer[num1] = answer[num2]
    answer[num2] = temp
    
    my_string = "".join(answer)
    
    return my_string