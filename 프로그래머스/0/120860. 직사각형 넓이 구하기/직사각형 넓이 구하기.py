def solution(dots):
    answer = 0
    for i in range(1,len(dots)):
        dots[i][0] -= dots[0][0]
        dots[i][1] -= dots[0][1]
    answer = (dots[1][0]*dots[2][1]-dots[1][1]*dots[2][0])
    if(answer< 0):
        answer = -answer
    return answer