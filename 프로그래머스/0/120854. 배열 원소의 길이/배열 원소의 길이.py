def solution(strlist):
    answer = []
    count = 0
    for i in strlist:
        for j in i:
            count += 1
        answer.append(count)
        count = 0
    return answer