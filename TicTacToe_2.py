"""
    - Are there better ways to read inputs and make sure it is what you want
        -instead of a bunch of if statments?
    - Don't know if the way I kept asking (if incorrect input) was the best way.
        -Ran into problems of function not returning or returning the incorrect info
    - I think the board is a global var - if it is IDK how else to initiate just in the first loop
        - Did not want to keep re clearing the board when loop was running
    - setting up Python for loops confuse me

"""
import numpy


def printboard(board):
    for boardrow in board:
        print(f'{boardrow[0]}|{boardrow[1]}|{boardrow[2]}')

def updateboard(m,n,board,player):
    if player == 1:
        board[m][n] = "X"
        printboard(board)
    else:
        board[m][n] = "O"
        printboard(board)


#NEED TO MAKE A WHILE LOOP INSTEAD OF RECALLING FUNCTIONS BC IF BAD INPUT THE RETURNS WILL NOT END AND THEREFORE CAUSE ERRORS


def askplayer(player,board):
    m = 0
    n = 0
    loopend = False

    while(loopend == False):
        if player == 0:
            inp = inputcheck(input("Player 1: Input row and column values. ex: '1,2' "),player,board)
        else:
            inp= inputcheck(input("Player 2: Input row and column values as a tuple. ex: '1,2' "),player,board)

        if inp != False:
            loopend = True
            return(inp)

def inputcheck(inp,player,board):
    #print(inp)
    if len(inp) == 3:
        if inp[1] == ",":
            if inp[0].isnumeric() and inp[2].isnumeric():
                m = int(inp[0])
                n = int(inp[2])
                if (0 <= m <=2) and (0 <= n <=2):
                    if board[m][n] == "_":
                        return (m, n)
                    else:
                        print("Location already filled. Try again.")
                        return (False)
                else:
                    print("Please input a number 0 thorugh 2")
                    return(False)
            else:
                print("Ensure row and columns are numbers")
                return(False)
        else:
            print("Invalid input. Try again")
            return(False)
    else:
        print("Invalid input. Try again")
        return(False)

def checkforwin(board):
    #Checks horizontal wins
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[0] != "_":
            return(row[0])
    #Checks vertical wins
    for col in numpy.transpose(board):
        if col[0] == col[1] and col[1] == col[2]  and col[0] != "_":
            return(col[0])
    #Checks diagonal wins
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
        return(board[0][0])
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != "_":
        return(board[0][2])


board = [["_","_","_"],
         ["_","_","_"],
         ["_","_","_"]]

for k in range(9):
    if ((k) % 2) == 0:
        player = 0
    else:
        player = 1

    m,n = askplayer(player,board)
    updateboard(m,n,board,player)
    winner = checkforwin(board)
    if winner == "X":
        print("Player 2 wins!")
        break
    elif winner == "O":
        print("Player 1 wins!")
        break
    elif k == 8:
        print("It's a tie!")