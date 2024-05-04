def solution(numbers, k):
    answer = 0
    for i in range(0,k):
        answer = numbers[(i*2)%len(numbers)]
    return answer 