def solution(my_string, is_prefix):
    answer = 0
    a = ''
    for i in my_string:
        a += i
        if (a == is_prefix):
            answer = 1
    return answer