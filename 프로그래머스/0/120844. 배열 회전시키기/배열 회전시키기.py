def solution(numbers, direction):
    answer = []
    if(direction=="left"):
        for i in range(len(numbers)):
            answer.append(numbers[(i+1)%len(numbers)])
    elif(direction=="right"):
        for i in range(len(numbers)):
            answer.append(numbers[(i+len(numbers)-1)%len(numbers)])
    return answer