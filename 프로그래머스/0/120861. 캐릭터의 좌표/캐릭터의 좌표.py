def x_check(x,board):
    if (x > board[0]//2):
        x = board[0]//2
    elif(-(board[0]//2) > x ):
        x = -(board[0]//2)
    return x

def y_check(y,board):
    if (y > board[1]//2):
        y = board[1]//2
    elif(-(board[1]//2) >y):
        y = -(board[1]//2)
    return y

def solution(keyinput, board):
    answer = []
    x = 0
    y = 0
    for i in keyinput:
        if (i == "left"):
            x -= 1
            x = x_check(x,board)
        elif (i == "right"):
            x += 1
            x = x_check(x,board)
        elif (i == "up"):
            y += 1
            y = y_check(y,board)
        elif (i == "down"):
            y -= 1
            y = y_check(y,board)
        elif( i == '' ):
            break
            
    
    answer.append(x)
    answer.append(y)
    return answer