def solution(n):
    num = 1
    answer = 0
    while num <= n:
        num = num*(answer+1)
        answer += 1
        
    return answer-1