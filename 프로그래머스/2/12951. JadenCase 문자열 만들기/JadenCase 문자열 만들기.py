def solution(s):
    answer = ''
    w = s.split(" ")
    for i in w:
        answer += i.capitalize()
        answer += ' '
    answer = answer[:-1]
    return answer