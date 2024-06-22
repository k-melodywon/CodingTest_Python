def solution(myString, pat):
    answer = 0
    table = str.maketrans('AB', 'BA')
    pat = pat.translate(table)
    if (myString.find(pat) != -1):
        answer = 1
    return answer