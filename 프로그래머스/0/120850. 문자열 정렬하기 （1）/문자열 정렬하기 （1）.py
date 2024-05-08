import re

def solution(my_string):
    
    answer = []
    my_string = re.sub(r'[^0-9]', '',my_string)
    
    for i in my_string:
        answer.append(int(i))
        
    answer.sort()
    return answer