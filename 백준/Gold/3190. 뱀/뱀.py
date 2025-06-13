n = int(input())
apple_num = int(input())
apple_loc = [list(map(int, input().split())) for _ in range(apple_num)]
snake = int(input())
snake_len = 1
count = 0
snake_dir = []
snake_load = []* snake_len
x = 1
y = 1
## 북 0 동 1 남 2 서 3
snake_head = 1

## 북동남서
##dx = [0 , 1 , 0 , -1]
##dy = [-1 , 0 , 1 , 0] 기존 방법 틀림 이유 이해하자
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

## nxn 배열 만들기
map = [[0 for _ in range(n+2)] for _ in range(n+2)]
for i in range(n+2):
    map[0][i] = 1
    map[n+1][i] = 1
    map[i][0] = 1
    map[i][n+1] = 1

## 새로운 배열 받기 방법 외우기
for _ in range(snake):
    t, c = input().split()
    t = int(t)
    snake_dir.append((t, c))

## 맵: 0 벽:1 사과:2 뱀:3
for i in apple_loc:
    map[i[0]][i[1]] = 2

snake_load.append([1,1])

def over(x, y, snake_head, map, snake_load):
    # 복사하여 뱀의 위치를 나타내는 코드
    temp = [row[:] for row in map]
    for i in range(len(snake_load)):
        temp[snake_load[i][0]][snake_load[i][1]] = 3
    
    for i in range(len(snake_dir)):
        
        if count == snake_dir[i][0]:
           
            if snake_dir[i][1] == 'D':
               snake_head = (snake_head+1)%4
            if snake_dir[i][1] == 'L':
                snake_head = (snake_head+3)%4

    if temp[x+dx[snake_head]][y+dy[snake_head]] == 1 or temp[x+dx[snake_head]][y+dy[snake_head]] == 3:
        print(count+1)
        return False
    return True

while over(x, y, snake_head, map, snake_load) == True:

    for i in range(len(snake_dir)):
        
        if count == snake_dir[i][0]:
           
            if snake_dir[i][1] == 'D':
               snake_head = (snake_head+1)%4
            if snake_dir[i][1] == 'L':
                snake_head = (snake_head+3)%4


    x = x + dx[snake_head]
    y = y + dy[snake_head]
    snake_load.append([x,y])

    if map[x][y] == 2:
        snake_len += 1
        map[x][y] = 0

    if len(snake_load) > snake_len:
        del snake_load[0]


    count = count + 1
