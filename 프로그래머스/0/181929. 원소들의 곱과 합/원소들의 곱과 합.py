def solution(num_list):
    answer = 0
    multiply = 1
    plus = 0
    for i in num_list:
        multiply *= i
        
    for i in num_list:
        plus += i
    
    if(multiply<(plus*plus)):
        answer = 1
        
    return answer