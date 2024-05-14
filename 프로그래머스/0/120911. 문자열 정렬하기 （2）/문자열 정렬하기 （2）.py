def solution(my_string):
    a = ""
    answer = my_string.lower()
    answer = list(answer)
    answer.sort()
    for i in range(len(answer)):
        a = a + str(answer[i])
    return a