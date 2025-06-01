w, l = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(w)]

# 북, 동, 남, 서 (시계 방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:
    # 1. 현재 칸 청소 안 됐으면 청소
    if arr[x][y] == 0:
        arr[x][y] = 2
        count += 1

    cleaned = False

    # 2. 4방향 중 왼쪽부터 확인
    for _ in range(4):
        d = (d + 3) % 4  # 왼쪽 방향
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < w and 0 <= ny < l and arr[nx][ny] == 0:
            x, y = nx, ny
            cleaned = True
            break

    if not cleaned:
        # 후진
        bx = x - dx[d]
        by = y - dy[d]

        if 0 <= bx < w and 0 <= by < l and arr[bx][by] != 1:
            x, y = bx, by
        else:
            break

print(count)

