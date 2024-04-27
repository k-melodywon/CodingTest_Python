def solution(num_list):
    answer = [0]*len(num_list)
    j=1
    for i in num_list:
        answer[len(num_list)-j]=i
        j+=1
    return answer