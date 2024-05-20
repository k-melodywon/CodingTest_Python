def solution(cipher, code):
    answer = ''
    count = 0
    for i in cipher:
        count += 1
        if (count==code):
            answer += i
            count = 0
    return answer