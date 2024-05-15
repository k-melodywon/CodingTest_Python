def solution(s):
    answer = ''
    count = 0
    for i in s:
        for j in s:
            if (i==j):
                count += 1
        if (count==1):
            answer = answer + i
        count = 0
    answer = list(answer)
    answer.sort()
    return "".join(answer)