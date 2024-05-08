import re

def solution(my_string):
    
    answer = 0
    my_string = re.sub(r'[^0-9]', '',my_string)
    
    for i in my_string:
        answer = answer + int(i)
    return answer