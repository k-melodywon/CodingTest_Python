from collections import deque

# 이동 방향 설정: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy, board):
    count = 0
    # 다음 위치가 벽이 아니고 구멍이 아닐 때까지 이동한다.
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
        if board[x][y] == 'O':
            break
    return x, y, count

def bfs(board, rx, ry, bx, by):
    n, m = len(board), len(board[0])
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = True

    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth >= 10:
            return -1
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], board)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], board)

            # 파란 구슬이 구멍에 빠진 경우
            if board[nbx][nby] == 'O':
                continue
            # 빨간 구슬이 구멍에 빠진 경우 성공
            if board[nrx][nry] == 'O':
                return depth + 1

            # 두 구슬이 같은 위치에 있는 경우 처리
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth + 1))
    return -1

def main():
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    rx = ry = bx = by = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
                board[i][j] = '.'
            elif board[i][j] == 'B':
                bx, by = i, j
                board[i][j] = '.'
    result = bfs(board, rx, ry, bx, by)
    print(result)

if __name__ == '__main__':
    main()

