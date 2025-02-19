def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    answer = myString.find(pat)
    if answer == -1 :
        answer = 0
    else:
        answer = 1
    return answer