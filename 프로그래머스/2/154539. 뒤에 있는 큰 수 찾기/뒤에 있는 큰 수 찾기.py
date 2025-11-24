"""def solution(numbers):
    answer = []
    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[j] > numbers[i] :
                answer.append(numbers[j])
                break
            if j == len(numbers)-1 :
                answer.append(-1)

    answer.append(-1)
    return answer
"""

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []  # 인덱스를 넣는 스택
    
    for i in range(len(numbers)):
        # 현재 수가 스택 top보다 크면 → 답 갱신
        while stack and numbers[i] > numbers[stack[-1]]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        
        stack.append(i)
    
    return answer
