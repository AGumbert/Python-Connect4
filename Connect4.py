#USE IDLE, NOT THE AOPS WINDOW

#code that will increase the program's time limit, but is not needed in idle:
#import sys
#sys.setExecutionLimit(1000000)

moves = 0#initializes a variable that counts how many moves have passed
whoseTurn = 1#initializes a variable that tracks whose turn it is (1 = player 1 or X, 2 = player 2 or O)
gameBoard = []#initializes the variable that stores who has what spaces in the gameboard
winner = 'nobody'#initializes the variable that keeps track of who wins (0 = nobody yet, 1 = X, 2 = O) 

#Sets each space in the gameboard to '.', showing that nobody has any of the spaces yet
for i in range(42):
    gameBoard.append(".")

#This function sets up the game with the player's names and gives the option of displaying instructions
def Setup():

    #asks the player whether he or she wants instructions
    response1 = ''
    while response1 != "play" and response1 != "information":#loops the asking until the response is either 'play' or 'instructions'
        response1 = input("Welcome to Connect Four! To get instructions, type 'information'. To begin a game immediately, type 'play'.")
    if response1 == "information":#prints out the game's instructions
        print("In this game, two players will alternate selecting columns on a game board to try to get four spaces in a row. With each selection, the furthest down available space in the selected column will go to the player who made the selection. As soon as four spaces in a row belong to one player, that player wins.")

    #Asks for the player's names    
    player1 = input("Enter the name of player one:")
    player2 = input("Enter the name of player two:")

    #Gives the players information on how they set up the game
    print("You have now set up a game with " + player1 + " as player one (X) and " + player2 + " as player two (O).")

    #returns the player's names
    return [player1, player2]

#sets up a variable to store the names of the players
pNames = Setup()

#the function that runs for every time a player takes a turn
def TakeTurn():

    #Initiation of variables inside the function:
    global whoseTurn
    global moves
    lowestDown = "Full"#This gets set to the lowest down space in the column selected
    
    
    selection = input("Now it's " + pNames[whoseTurn - 1] +"'s turn. Enter a column number (0-6) to select it as your move:")#asks for the column selection and sets selection to the input

    #continues asking for a different column if the input is not a valid number from 1-6
    while selection != "0" and selection != "1" and selection != "2" and selection != "3" and selection != "4" and selection != "5" and selection != "6":
        selection = input("Not a valid column! Pick another one (0-6):")

    #converts selection to an integer for future use
    selection = int(selection)

    #this loop finds the lowest down space in the selected column and asks for a new column if the selected column is full
    while lowestDown == "Full":
        
        #sets lowest down to the lowest space that is a '.' in the selected column by looping through and checking each space from the top of the column to the bottom
        for i in range(6):
            if gameBoard[selection+i*7] == ".":
                lowestDown = i
                
        #If the lowest down is still full after checking each space in the column, ask for a new column and then convert the input to an integer
        if lowestDown == "Full":
            while selection != "0" and selection != "1" and selection != "2" and selection != "3" and selection != "4" and selection != "5" and selection != "6": 
                selection = input("Not a valid column! Pick another one (0-6):")
            selection = int(selection)

    #if it is player 1's turn, make it player 2's turn and fill the selected column's lowest space with and 'X'
    if whoseTurn == 1:
        whoseTurn = 2
        gameBoard[selection+lowestDown*7] = "X"

     #if it is player 2's turn, make it player 1's turn and fill the selected column's lowest space with and 'O'           
    else:
        whoseTurn = 1
        gameBoard[selection+lowestDown*7] = "O"

    #prints out the board after the turn is completed
    board = "0 1 2 3 4 5 6\n"#initializes the board print variable with the first row

    #adds each space in the gameBoard variable to the board variable with a nested for loop
    for i in range(6):#for every row
        for j in range(7):#for every column
            board += gameBoard[j+i*7] + " "#adds the information from gameBoard to board
        board += "\n"#ncreates a new line for each new row
    print("Now the board looks like this:\n" + board)#prints the results

    moves += 1#counts the moves by adding one more

#the function that checks for a winner or for a tie
def checkForWinner():
    winner = 'nobody'#initializes the winner variable to be returned with information about who has won

    #if the moves reaches 42, there is a tie
    if moves == 42:
        winner = 'tie'

    #only the first check is commented because all use essentially the same algorithm. 

    #checks for four X's in a horizontal row
    for i in range (4):#for column
        for j in range (6):#for row
            check1 = True#initializes a variable that is set to false if the row being checked is not completely X's
            for k in range (4):#for the four spaces required to get four in a row
                if gameBoard[i+7*j+k] != "X":#set check1 to false if one space in the row is not X
                    check1 = False
            if check1 == True:#if check1 is still true, X wins
                winner = 'X'

    #checks for four O's in a horizontal row
    for i in range (4):
        for j in range (6):
            check1 = True
            for k in range (4):
                if gameBoard[i+7*j+k] != "O":
                    check1 = False
            if check1 == True:
                winner = 'O'

    #checks for four X's in a vertical row
    for i in range (7):
        for j in range (3):
            check1 = True
            for k in range (4):
                if gameBoard[i+7*j+k*7] != "X":
                    check1 = False
            if check1 == True:
                winner = 'X'

    #checks for four O's in a vertical row
    for i in range (7):
        for j in range (3):
            check1 = True
            for k in range (4):
                if gameBoard[i+7*j+k*7] != "O":
                    check1 = False
            if check1 == True:
                winner = 'O'

    #checks for four X's in a '\' oriented diagonal row 
    for i in range (4):
        for j in range (3):
            check1 = True
            for k in range (4):
                if gameBoard[i+7*j+k*8] != "X":
                    check1 = False
            if check1 == True:
                winner = 'X'

    #checks for four O's in a '\' oriented diagonal row 
    for i in range (4):
        for j in range (3):
            check1 = True
            for k in range (4):
                if gameBoard[i+7*j+k*8] != "O":
                    check1 = False
            if check1 == True:
                winner = 'O'

    #checks for four X's in a '/' oriented diagonal row 
    for i in range (4):
        for j in range (3):
            check1 = True
            for k in range (4):
                if gameBoard[3+i+7*j+k*6] != "X":
                    check1 = False
            if check1 == True:
                winner = 'X'

    #checks for four O's in a '/' oriented diagonal row 
    for i in range (4):
        for j in range (3):
            check1 = True
            for k in range (4):
                if gameBoard[3+i+7*j+k*6] != "O":
                    check1 = False
            if check1 == True:
                winner = 'O'

    return winner

#prints out the first board, before any players have moved
board = "0 1 2 3 4 5 6\n"#initializes the board variable to be printed with the first row
for i in range(6):#for every row
    for j in range(7):#for every column
        board += ". "#add a ". "
    board += "\n"#start a new row
print("Now the board looks like this:\n" + board)#print the results

while winner == 'nobody':#while nobody has won
    TakeTurn()#take a turn
    winner = checkForWinner()#check for a winner

#congratulate X if X wins
if winner == 'X':
    print("And " + pNames[0] + " is the winner after " + str(moves) + " total moves were made!\nCongratulations!")

#congratulates O if O wins
if winner == 'O':
    print("And " + pNames[1] + " is the winner after " + str(moves) + " total moves were made!\nCongratulations!")

#prints a message if there is a tie
if winner == 'tie':
    print("And it's a tie! No one managed to connect four before all spaces were used up.")





