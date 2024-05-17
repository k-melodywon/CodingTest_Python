def solution(common):
    answer = 0
    try:
        if(common[1]/common[0]==common[2]/common[1]):
            answer = common[len(common)-1]*(common[1]/common[0])
        elif(common[1]-common[0]==common[2]-common[1]):
            answer = common[len(common)-1] + (common[1]-common[0])
    except:
        answer = common[len(common)-1] + (common[1]-common[0])
    return answer