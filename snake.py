import random
board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

moving = ""



def display():
    for line in board:
        print(line)
    print("----------------------------------------------")

def create_head():
    x=random.randint(0, len(board)-1)
    y=random.randint(0, len(board)-1)
    board[x][y]=1

def create_apple():
    x=random.randint(0, len(board)-1)
    y=random.randint(0, len(board)-1)
    if board[x][y]==0:
        board[x][y]= -1
    else:
        create_apple








display()
create_head()
create_apple()
display()