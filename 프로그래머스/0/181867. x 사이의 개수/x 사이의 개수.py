def solution(myString):
    answer = []
    count = 0
    list = myString.split('x')
    for i in list:
        for j in i:
            count += 1
        answer.append(count)
        count = 0
        
    return answer