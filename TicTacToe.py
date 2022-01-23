
"""
Challenges for the week:
    - Figure out how to represent the game board --- A 3x3 Matrix
    - Print an individual game board --- Use print command of each row to help see the board (couldnt find a better way other than numpy but that didnt work for some reason)
    - Create a list of moves and manually represent the game state after each move --- reprint board after moves
    - Create a system for handling illegal moves (will need to throw errors) --- series of if statements for illegal moves
    - Create a way to take human input to _create_ moves --- Specify who is playing with print (Player A or B) and ask for a position to play
    - Play a game of tic tac toe against yourself.
"""
#print("Good luck and may the odds forever be in your favor")

"""
Comments:
    - Couldn't think of a way to dynamically look for a win
    - Could not get threads to work (the way I wanted) - Want to try get/set or global var
    - Never have known what to do with for/counter variables and the etiquette of their names
    - Thought of maybe using a for loop with ifs asking if the for # is odd it asks player 1 and if even asks player 2
        + Then the game will end at certain # of moves or the loop will break if someone wins
    - Don't have comments on it and I know I should need them
"""

"""
import _thread

def win_check(check, playerid):
    if check == 1:
        if playerid == "X":
            print("Player 1 wins!")

        elif matrix[a][0] == "O":
            print("Player 2 wins!")
        _thread.start_new_thread(win_check, (win,playerid))
"""
x = False
y = False
finish = False
count = 0
win = 0
playerid = "_"

matrix = [["_","_","_"],
          ["_","_","_"],
          ["_","_","_"]]

displaymatrix = [["1","2","3"],
                 ["4","5","6"],
                 ["7","8","9"]]

print("Below shows the TicTacToe board and locations to play")

print(displaymatrix[0])
print(displaymatrix[1])
print(displaymatrix[2])

while finish == False:
    x = False
    y = False

    while x == False:



        player1loc = input("Player One's turn: select location to play")
        if player1loc == "1" or player1loc == "2" or player1loc == "3" or player1loc == "4" or player1loc == "5" or player1loc == "6" or player1loc == "7" or player1loc == "8" or player1loc == "9":

            for rowx in range(3):
                for colx in range(3):
                    if displaymatrix[rowx][colx] == player1loc:
                        if matrix[rowx][colx] != "_":
                            print("Location is already filled")
                        else:
                            matrix[rowx][colx] = "X"
                            x = True


        else:
            print("Incorrect input. Try Again")

    for a in range(3):
        if matrix[a][0] == matrix[a][1] and matrix[a][0] == matrix[a][2]:
            if matrix[a][0] == "X":
                print("Player 1 wins!")
                win = True

            elif matrix[a][0] == "O":
                print("Player 2 wins!")
                win = True

    for b in range(3):
        if matrix[0][b] == matrix[1][b] and matrix[0][b] == matrix[2][b]:
            if matrix[0][b] == "X":
                print("Player 1 wins!")
                win = True
            elif matrix[0][b] == "O":
                print("Player 2 wins!")
                win = True

    if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
        if matrix[0][0] == "X":
            print("Player 1 wins!")
            win = True
        elif matrix[0][0] == "O":
            print("Player 2 wins!")
            win = True

    if matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:
        if matrix[0][2] == "X":
            print("Player 1 wins!")
            win = True
        elif matrix[0][2] == "O":
            print("Player 2 wins!")
            win = True

    print(matrix[0])
    print(matrix[1])
    print(matrix[2])

    count = count + 1

    if count == 9:
        print("Game ended in a tie!")
        break
    if win == True:
        break
    if count < 9:
        while y == False:
            player2loc = input("Player Two's turn: select location to play")
            if player2loc == "1" or player2loc == "2" or player2loc == "3" or player2loc == "4" or player2loc == "5" or player2loc == "6" or player2loc == "7" or player2loc == "8" or player2loc == "9":
                #player1loc = int(player1loc)

                for rowo in range(3):
                    for colo in range(3):
                        if displaymatrix[rowo][colo] == player2loc:
                            if matrix[rowo][colo] != "_":
                                print("Location is already filled")
                            else:
                                matrix[rowo][colo] = "O"
                                y = True


            else:
                print("Incorrect input. Try Again")

        print(matrix[0])
        print(matrix[1])
        print(matrix[2])

        for a in range(3):
            if matrix[a][0] == matrix[a][1] and matrix[a][0] == matrix[a][2]:
                if matrix[a][0] == "X":
                    print("Player 1 wins!")
                    win = True
                elif matrix[a][0] == "O":
                    print("Player 2 wins!")
                    win = True
        for b in range(3):
            if matrix[0][b] == matrix[1][b] and matrix[0][b] == matrix[2][b]:
                if matrix[0][b] == "X":
                    print("Player 1 wins!")
                    win = True
                elif matrix[0][b] == "O":
                    print("Player 2 wins!")
                    win = True

        if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
            if matrix[0][0] == "X":
                print("Player 1 wins!")
                win = True
            elif matrix[0][0] == "O":
                print("Player 2 wins!")
                win = True

        if matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:
            if matrix[0][2] == "X":
                print("Player 1 wins!")
                win = True
            elif matrix[0][2] == "O":
                print("Player 2 wins!")
                win = True

        count = count + 1


        if win == True:
            finish = True


#print("Location Specified has already been filled. Try again.")

"""
while x == False:
    p1r = input("Player one's turn: select row in index notation (0-2)")

    if p1r == "0" or p1r == "1" or p1r == "2":
        p1r = int(p1r)
        x = True
    else:
        print("Incorrect input. Try Again")

while y == False:
    p1c = input("Player one's turn: select column in index notation (0-2)")

    if p1c == "0" or p1c == "1" or p1c == "2":
        p1c = int(p1c)
        y = True
    else:
        print("Incorrect input. Try Again")
"""






#sup