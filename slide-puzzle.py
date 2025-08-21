# slide puzzle
import random
import os
'''
1 2 3
4 5 6
7 8
'''
def draw_board(board):
    print(f"{board[0]} {board[1]} {board[2]}")  #board[2]=1
    print(f"{board[3]} {board[4]} {board[5]}")  #board[5]=" "
    print(f"{board[6]} {board[7]} {board[8]}")


board=[1,2,3,4,5,6,7,8," "]
random.shuffle(board)
print(board)
def box_pos():
    i=" "
    for i in range(len(board)):
        if board[i]==" ":
            return int(i)
print(box_pos())
def player_move():
    y=box_pos()
    if move in ['u','d']:
        x=3
    elif move in ['l','r']:
        x=1
    else:
        x=0
    if move=='u' and y not in [0,1,2]:
        board[y],board[y-x]=board[y-x],board[y]
    elif move=='d' and y not in [6,7,8]:
        board[y],board[y+x]=board[y+x],board[y]
    elif move=='l' and y not in [0,3,6]:
        board[y],board[y-x]=board[y-x],board[y]
    elif move=='r' and y not in [2,5,8]:
        board[y],board[y+x]=board[y+x],board[y]
    print(y,x)
    return board
draw_board(board)
while True:

    os.system('cls' if os.name=='nt' else 'clear')
    draw_board(board)
    move=input("Enter your move(up/down/left/right): ")
    player_move()
    draw_board(board)

