def solution(array, n):
    answer = 0
    array.sort()
    temp = array[:]
    for i in range(0,len(temp)):
        temp[i] -= n 
        if (temp[i]<0):
            temp[i]= -temp[i]
    answer = array[temp.index(min(temp))] 
    return answer