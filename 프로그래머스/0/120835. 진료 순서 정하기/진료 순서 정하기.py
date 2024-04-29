def solution(emergency):
    answer = []
    over = 1
    for i in emergency:
        for j in range(len(emergency)):
            if (emergency[j]>i):
                over+=1
        answer.append(over)
        over = 1
    return answer