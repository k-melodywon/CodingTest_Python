def solution(topping):
    answer = 0
    n = len(topping)
    left_set = set()
    right_set = set()
    left_unique_count = [0] * n
    right_unique_count = [0] * n
    
    for i in range(n):
        left_set.add(topping[i])
        left_unique_count[i] = len(left_set)
        
    for i in range(n-1, -1, -1):
        right_set.add(topping[i])
        right_unique_count[i] = len(right_set)
    
    for i in range(n-1):
        if left_unique_count[i] == right_unique_count[i+1]:
            answer += 1
    
    return answer
