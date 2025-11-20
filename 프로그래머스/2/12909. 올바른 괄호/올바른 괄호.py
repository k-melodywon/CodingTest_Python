#def solution(s):
    
    #answer = True
    
   # while s.find("()") != -1:
    #    s = s.replace("()","")
    
    
   # if s == '':
  #      answer = True
 #   else:
#        answer = False
    
#    return answer

def solution(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:  # ')'
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0
