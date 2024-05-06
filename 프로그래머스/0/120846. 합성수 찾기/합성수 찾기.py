def solution(n):
    answer = 0
    check = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            if (i%j == 0):
                check += 1
        if (check>=3):
            answer += 1
            check = 0
        else:
            check = 0

    return answer