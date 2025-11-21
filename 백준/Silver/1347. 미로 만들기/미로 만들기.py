import sys
size = int(sys.stdin.readline().strip())
move = sys.stdin.readline().strip()
#아래 오른쪽 위 왼쪽로 이동하는 좌표
dx = [0, 1, 0 , -1]
dy = [-1,0 ,1, 0]
"""
바라보는 방향
0: 아래
1: 오른쪽
2: 위
3: 왼쪽
"""
d = 0

#현재 위치
x = 0
y = 0
load = []
load.append([x,y])
for i in move:
    if i == 'R':
        d = (d+3)%4
    if i == 'L':
        d = (d+1)%4
    if i == 'F':
        if d == 0:
            x = x +dx[0]
            y = y + dy[0]
            load.append([x,y])
        if d == 1:
            x = x + dx[1]
            y = y + dy[1]
            load.append([x,y])
        if d == 2:
            x = x + dx[2]
            y = y + dy[2]
            load.append([x,y])
        if d == 3:
            x = x + dx[3]
            y = y + dy[3]
            load.append([x,y])
min_x = 0
max_x = 0
#가로
l = 0
#세로
m = 0
for i in load:
    if i[0] > max_x:
        max_x = i[0]
for i in load:
    if i[0] < min_x:
        min_x = i[0]
l = max_x - min_x +1


min_y = 0
max_y = 0
for i in load:
    if i[1] > max_y:
        max_y = i[1]
for i in load:
    if i[1] < min_y:
        min_y = i[1]
m = max_y - min_y +1


grid = [['#'] * l for _ in range(m)]
for x, y in load:
    grid[max_y -y][x - min_x] = '.' 

for row in grid:
    print("".join(row))   
