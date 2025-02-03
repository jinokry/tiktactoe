import random

board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

currrent_player = "X"
winner = None
gameRunning = True


#print the game board
def printBpard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input
def playerInput(borad):
    inp = int(input("Enter a number between 1-9: "))
    if inp >= 1 and inp <=9 and board[inp-1] == "_":
        board[inp-1] = currrent_player
    else:
        print("Invaild input. check the board and try again.")
#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "_":
        winner = board[6]
        return True
    

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True
    
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True
    
def checkTie(board):
    if "_" not in board:
        printBpard(board)
        print("It's a tie!")
        gameRunning = False 
#switch the player

def checkTie(board):
    global gameRunning
    if "_" not in board:
        printBpard(board)
        print("It's a tie!")
        gameRunning = False

def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        printBpard(board)
        print(f"The winner is {winner}")
        gameRunning = False                 


def switchPlayer():
    global currrent_player
    if currrent_player == "X":
        currrent_player = "O"
    else:
        currrent_player = "X"

def computer(board):
    while currrent_player == "0":
        position = random.randint(0,8)
        if board[position] == "_":
            board[position] = "0"
            switchPlayer()
            break
        else:
            continue

#check for win or tie again
while gameRunning:
    printBpard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)

    