def solution(s):
    answer = []
    c0 = 0
    c1 = 0
    count = 0
    re_s = ''
    
    while s != "1" :
        c0 += s.count("0")
        s = s.replace("0", "")
        c1 = s.count("1")
        s = ''
        re_s = ''

        while c1 > 0:
            s += str(int(c1%2))
            c1 = c1//2
        for i in reversed(s):
            re_s += i
        s= ''
        s= re_s
        count +=1
    
    
    answer.append(count)
    answer.append(c0)
    
    return answer