def solution(num_list, n):
    answer = 0
    try:
        if(num_list.index(n) != -1):
            answer = 1
    except ValueError:
         return answer
        
    return answer