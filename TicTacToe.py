import random
print("Welcome to Tic Tac Toe")
board = [["-","-","-",], #initializes placeholder values for tic tac toe board
         ["-","-","-",],
         ["-","-","-"]]
def printBoard(board):
    """ prints board with updated values"""
    for x in board:
        for y in x:
            print(y, end="")
        print()
def numChecker(user_input):
    """ensures that user input is a number"""
    if not user_input.isnumeric():
        return False
    else:
        return True
def quit(user_input):
    """exits program if user enters q for quit"""
    if user_input.lower() == "q":
        return False
    else:
        return True
def userPlay(user_input):
    """
    subtracts user input by 1 in order for value to be used an index num
    depending on user input, an x will be placed on the board
    """
    user_input -= 1
    if user_input == 0:
        board[0][0] = "x"
    if user_input == 1:
        board[0][1] = "x"
    if user_input == 2:
        board[0][2] = "x"
    if user_input == 3:
        board[1][0] = "x"
    if user_input == 4:
        board[1][1] = "x"
    if user_input == 5:
        board[1][2] = "x"
    if user_input == 6:
        board[2][0] = "x"
    if user_input == 7:
        board[2][1] = "x"
    if user_input == 8:
        board[2][2] = "x"
def cpuPlay(cpuNum):
    """gets cpu random number and makes a play on the board for the computer player"""
    if cpuNum == 0:
        board[0][0] = "0"
    if cpuNum == 1:
        board[0][1] = "0"
    if cpuNum == 2:
        board[0][2] = "0"
    if cpuNum == 3:
        board[1][0] = "0"
    if cpuNum == 4:
        board[1][1] = "0"
    if cpuNum == 5:
        board[1][2] = "0"
    if cpuNum == 6:
        board[2][0] = "0"
    if cpuNum == 7:
        board[2][1] = "0"
    if cpuNum == 8:
        board[2][2] = "0"

def winCheckPlayer1():
    """checks for a winner after each turn"""
    if board[0][0] == "x":
        if board[0][1] == "x":
            if board[0][2] == "x":
                return True
    else:
        return False

def winCheckPlayer2():
    """ checks for a specific winning play"""
    if board[1][0] == "x":
        if board[1][1] == "x":
            if board[1][2] == "x":
                return True
    else:
        return False

def winCheckPlayer3():
    """ checks for a specific winning play"""
    if board[2][0] == "x":
        if board[2][1] == "x":
            if board[2][2] == "x":
                return True
    else:
        return False
def winCheckPlayer4():
    """ checks for a specific winning play"""
    if board[0][0] == "x":
        if board[1][0] == "x":
            if board[2][0] == "x":
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def winCheckPlayer5():
    """ checks for a specific winning play"""
    if board[0][1] == "x":
        if board[1][1] == "x":
            if board[2][1] == "x":
                return True
    else:
        return False
def winCheckPlayer6():
    """ checks for a specific winning play"""
    if board[0][2] == "x":
        if board[1][2] == "x":
            if board[2][2] == "x":
                return True
    else:
        return False
def winCheckPlayer7():
    """ checks for a specific winning play"""
    if board[0][0] == "x":
        if board[1][1] == "x":
            if board[2][2] == "x":
                return True
    else:
        return False
def winCheckPlayer8():
    """ checks for a specific winning play"""
    if board[0][2] == "x":
        if board[1][1] == "x":
            if board[2][0] == "x":
                return True
    else:
        return False

def winCheckCpu1():
    """ checks for a specific winning play"""
    if board[0][2] == "0":
        if board[1][1] == "0":
            if board[2][0] == "0":
                return True
    else:
        return False

def winCheckCpu2():
    """ checks for a specific winning play"""
    if board[0][2] == "0":
        if board[1][1] == "0":
            if board[2][0] == "0":
                return True
    else:
        return False

def winCheckCpu3():
    """ checks for a specific winning play"""
    if board[0][2] == "0":
        if board[1][1] == "0":
            if board[2][0] == "0":
                return True
    else:
        return False
def winCheckCpu4():
    """ checks for a specific winning play"""
    if board[0][2] == "0":
        if board[1][1] == "0":
            if board[2][0] == "0":
                return True
    else:
        return False
def winCheckCpu5():
    """ checks for a specific winning play"""
    if board[0][2] == "0":
        if board[1][1] == "0":
            if board[2][0] == "0":
                return True
    else:
        return False
def winCheckCpu6():
    """ checks for a specific winning play"""
    if board[0][2] == "0":
        if board[1][1] == "0":
            if board[2][0] == "0":
                return True
    else:
        return False
def winCheckCpu7():
    """ checks for a specific winning play"""
    if board[0][2] == "0":
        if board[1][1] == "0":
            if board[2][0] == "0":
                return True
    else:
        return False
def winCheckCpu8():
    """ checks for a specific winning play"""
    if board[0][2] == "0":
        if board[1][1] == "0":
            if board[2][0] == "0":
                return True
    else:
        return False
def spotTaken(input):
    """ensures that the spot on the board is not taken before making a play"""
    input -= 1
    if input == 0 and board[0][0] == "-":
        return False
    elif input == 0 and board[0][0] != "-":
        return True
    if input == 1 and board[0][1] == "-":
        return False
    elif input == 1 and board[0][1] != "-":
        return True
    if input == 2 and board[0][2] == "-":
        return False
    elif input == 2 and board[0][2] != "-":
        return True
    if input == 3 and board[1][0] == "-":
        return False
    elif input == 3 and board[1][0] != "-":
        return True
    if input == 4 and board[1][1] == "-":
        return False
    elif input == 4 and board[1][1] != "-":
        return True
    if input == 5 and board[1][2] == "-":
        return False
    elif input == 5 and board[1][2] != "-":
        return True
    if input == 6 and board[2][0] == "-":
        return False
    elif input == 6 and board[2][0] != "-":
        return True
    if input == 7 and board[2][1] == "-":
        return False
    elif input == 7 and board[2][1] != "-":
        return True
    if input == 8 and board[2][2] == "-":
        return False
    elif input == 8 and board[2][2] != "-":
        return True

def spotTakenCpu(input):
    """ensures that the spot is free before the computer player makes a move"""
    if input == 0 and board[0][0] == "-":
        return False
    elif input == 0 and board[0][0] != "-":
        return True
    if input == 1 and board[0][1] == "-":
        return False
    elif input == 1 and board[0][1] != "-":
        return True
    if input == 2 and board[0][2] == "-":
        return False
    elif input == 2 and board[0][2] != "-":
        return True
    if input == 3 and board[1][0] == "-":
        return False
    elif input == 3 and board[1][0] != "-":
        return True
    if input == 4 and board[1][1] == "-":
        return False
    elif input == 4 and board[1][1] != "-":
        return True
    if input == 5 and board[1][2] == "-":
        return False
    elif input == 5 and board[1][2] != "-":
        return True
    if input == 6 and board[2][0] == "-":
        return False
    elif input == 6 and board[2][0] != "-":
        return True
    if input == 7 and board[2][1] == "-":
        return False
    elif input == 7 and board[2][1] != "-":
        return True
    if input == 8 and board[2][2] == "-":
        return False
    elif input == 8 and board[2][2] != "-":
        return True

while True:
    user_input = input("Enter number 1-9 or 'q' to quit: ") #gets user input
    if not quit(user_input): #if player presses q the program will exit, if not it will continue
        print("Goodbye")
        break
    if not numChecker(user_input): #checks for valid numeric input
        print("Please enter valid value")
        continue
    if spotTaken(int(user_input)): #ensures spot on board is free
        print("The spot has been taken! Press q if board is full.")
        continue
    userPlay(int(user_input)) #after the input is verified, the play is made on the board
    cpuNum = random.randint(0, 8) #a random cpu is generated to make a play
    for i in range(30): #ensures that if the spot is taken, a new cpu number is generated
        if spotTakenCpu(cpuNum):
            cpuNum = random.randint(0, 8)
    printBoard(board) #prints board after each turn
    #The following functions check for all possible winning combos.
    #if no winning combos are detected the game will continue
    if winCheckPlayer1():
        print("Game Over!")
        break
    else:
        pass
    if winCheckPlayer2():
        print("Game Over!")
        break
    else:
        pass
    if winCheckPlayer3():
        print("Game Over!")
        break
    else:
        pass
    if winCheckPlayer4():
        print("Game Over!")
        break
    else:
        pass
    if winCheckPlayer5():
        print("Game Over!")
        break
    else:
        pass
    if winCheckPlayer6():
        print("Game Over!")
        break
    else:
        pass
    if winCheckPlayer7():
        print("Game Over!")
        break
    else:
        pass
    if winCheckPlayer8():
        print("Game Over!")
        break
    else:
        pass
    cpuPlay(cpuNum)
    printBoard(board)
    if winCheckCpu1():
        print("Game Over!")
    else:
        pass
    if winCheckCpu2():
        print("Game Over!")
    else:
        pass
    if winCheckCpu3():
        print("Game Over!")
    else:
        pass
    if winCheckCpu4():
        print("Game Over!")
    else:
        pass
    if winCheckCpu5():
        print("Game Over!")
    else:
        pass
    if winCheckCpu6():
        print("Game Over!")
    else:
        pass
    if winCheckCpu7():
        print("Game Over!")
    else:
        pass
    if winCheckCpu8():
        print("Game Over!")
    else:
        continue



