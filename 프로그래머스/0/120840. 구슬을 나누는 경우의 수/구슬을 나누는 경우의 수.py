def solution(balls, share):
    answer = 0
    a = balls
    b = share
    for i in range(1,share):
        a = a*(balls-i)
        b = b*(share-i)
    return a/b