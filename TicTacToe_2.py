""" COMMENTS
    - How many functions are too many functions


"""


import math
import numpy as np

matrix = np.matrix([[0,0,0],[0,0,0],[0,0,0]])
displaymatrix = np.matrix([[7,8,9], [4,5,6] ,[1,2,3]])

def ask(playerturn):
    if math.ceil(playerturn/2) == playerturn/2:
        ask.playerloc = input("Player 1: choose a location to play.")
        ask.playerid = "X"
    elif math.ceil(playerturn/2) != playerturn/2:
        ask.playerloc = input("PLayer 2: choose a location to play")
        ask.playerid = "O"


def input_check(playerloc):
    if playerloc == "1" or playerloc == "2" or playerloc == "3" or playerloc == "4" or playerloc == "5" or playerloc == "6" or playerloc == "7" or playerloc == "8" or playerloc == "9":
        for row in range(2):
            for col in range(2):
                if displaymatrix[row][col] == playerloc:
                    if matrix[row][col] != 0:
                        print("Location is already filled. Try another location")
                    else:
                        matrix[row][col] = ask.playerid

    else:
        print("Invalid input. Please choose a valid location to play")


print(displaymatrix)
print("Above shows the TicTacToe board and locations to play")


for k in range(9):
    ask(k)
    input_check(ask.playerloc)


    print(ask.playerloc)