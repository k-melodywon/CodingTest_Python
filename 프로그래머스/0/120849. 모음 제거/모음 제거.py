def solution(my_string):
    answer = ''
    for i in my_string:
        if (i == 'a' or i == 'e' or i == 'i'  or i == 'o' or i == 'u' ):
            print("건너뛰기")
        else:
            answer = answer + i
    return answer