import random
import time
import msvcrt

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

moving = ""
length = 1
head_location = [0, 0]
apple_location = [0, 0]

def start_game():
    global moving
    create_head()
    create_apple()
    display()
    while moving != "b'w'" and moving != "b'a'" and moving != "b's'" and moving != "b'd'":
        get_start_input()
    move()

def get_start_input():
    global moving
    while moving == "":
        if msvcrt.kbhit(): 
            moving = str(msvcrt.getch())
        
    
    

def display():
    for line in board:
        print(line)
    print("----------------------------------------------")

def create_head():
    x=random.randint(0, len(board)-1)
    y=random.randint(0, len(board)-1)
    board[x][y]=1
    head_location[0]=x
    head_location[1]=y

def create_apple():
    x=random.randint(0, len(board)-1)
    y=random.randint(0, len(board)-1)
    if board[x][y]==0:
        board[x][y]= -1
        apple_location[0] = x
        apple_location[1] = y
    else:
        create_apple

def move():
    if moving == "b'a'":
        move_left()
    elif moving == "b'w'":
        move_up()
    elif moving == "b's'":
        move_down()
    elif moving == "b'd'":
        move_right()
    else:
        print("done")
    after_move()

def move_left():
    count = 0
    found = False
    while count < len(board) and (not found):
        in_count = 0
        while in_count < len(board[count]):
            if board[count][in_count] == 1 and in_count > 0 and board[count][in_count - 1] <= 0:
                board[count][in_count - 1] = 1
                head_location[1] -= 1
                found = True
                break
            elif board[count][in_count] == 1 and in_count == 0:
                game_over()
                break
            else:
                in_count+=1   
        count+=1

def move_up():
    count = 0
    found = False
    while count < len(board) and (not found):
        in_count = 0
        while in_count < len(board[count]):
            if board [count][in_count] == 1 and count > 0 and board[count-1][in_count] <= 0:
                board[count-1][in_count] = 1
                head_location[0] -= 1
                found = True
                break
            elif board[count][in_count] == 1 and count == 0:
                game_over()
                break
            else:
                in_count+=1
        count+=1

def move_down():
    count = 0
    found = False
    while count < len(board) and (not found):
        in_count = 0
        while in_count < len(board[count]):
            if board[count][in_count] == 1 and count < len(board)-1 and board[count + 1][in_count] <= 0:
                board[count+1][in_count] = 1
                head_location[0] += 1
                found = True
                break
            elif board[count][in_count] == 1 and count == len(board) - 1:
                game_over()
                break
            else:
                in_count+=1
        count+=1

def move_right():
    print("right")

def game_over():
    print("YOU LOSE")
    quit()

def after_move():
    count = 0
    while count < len(board):
        in_count = 0
        while in_count < len(board[count]):
            if board[count][in_count] > 0:
                board[count][in_count] += 1
            if board[count][in_count] > length:
                board[count][in_count] = 0
            board[head_location[0]][head_location[1]] = 1
            in_count+=1
        count+=1
    display()
    wait()

def between_moves():
    global moving
    if msvcrt.kbhit(): 
            moving = str(msvcrt.getch())

def wait():
    count = 0
    while count < 5:
        time.sleep(0.1)
        between_moves()
        count+=1
    move()
    










start_game()