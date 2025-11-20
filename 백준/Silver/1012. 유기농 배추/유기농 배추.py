import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())
results = []

for _ in range(T):
    M, N, K = map(int, input().split())  # M: 가로(0..M-1), N: 세로(0..N-1)
    grid = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1  # 주의: 입력은 (x, y) -> grid[y][x]

    visited = [[False]*M for _ in range(N)]
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    worms = 0

    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1 and not visited[r][c]:
                worms += 1
                # BFS 시작
                dq = deque()
                dq.append((r,c))
                visited[r][c] = True
                while dq:
                    cr, cc = dq.popleft()
                    for dr, dc in dirs:
                        nr, nc = cr+dr, cc+dc
                        if 0 <= nr < N and 0 <= nc < M:
                            if grid[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                dq.append((nr,nc))
    print(worms)
