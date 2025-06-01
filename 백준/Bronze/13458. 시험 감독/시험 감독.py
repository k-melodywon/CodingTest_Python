n = int(input())  # 시험장 개수
arr = list(map(int, input().split()))  # 각 반의 응시자 수
x, y = map(int, input().split())  # 감독관 수
a = 0

for i in arr:
    a += 1  # 총감독관은 반드시 1명
    if i > x:
        a += (i - x + y - 1) // y  # 정확한 올림 처리

print(a)