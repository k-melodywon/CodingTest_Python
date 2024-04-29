def solution(age):
    age = str(age)
    answer = ''
    age_list = ['a','b','c','d','e','f','g','h','i','j']
    
    for i in age:
        answer += age_list[int(i)]
    return answer