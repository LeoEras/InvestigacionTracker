import random
board = [" " for i in range(0, 36)]

def jump():
    for i in range(1, 50):
        print("\n")
        
def showMenu():
    options = ["H", "E", "L", "P", "h", "e", "l", "p"]
    print("**************************************************")
    print("******************** SENET ***********************")
    print("**************************************************")
    print("Press:")
    print("\'H\' to learn how to play")
    print("\'P\' to play game")
    print("\'L\' to load game")
    print("\'E\' to exit game")
    choice = raw_input("Your choice: ")
    while(choice not in options):
        choice = raw_input("Your choice: ")
    return choice

def printHelp():
    print("HOW TO PLAY:")
    print("At the start of each game you\'ll be given 5 tokens")
    print("they might be black or white.")
    print("The player assigned as Player 1 moves the black ones,")
    print("the other one moves the rest.")
    print("The first player who gets all his tokens out of the")
    print("board wins.")
    print("\nRULES: ")
    print("1.- You can move forward or backward as long as there")
    print("are not two kinds of the opposite player\'s token where")
    print("you go.")
    print("2.- If you fall to the Nile River, position 27 on the")
    print("board, you\'ll have to go back to position 15. If it\'s")
    print("occupied by any kind of token, you\'ll have to go back")
    print("until the first free position is reached.")
    print("3.- In order to get a token out of the board, your throw")
    print("has to be exact. And there must not be tokens of yours at")
    print("the first row.")
    print("4.- A token of yours can swap positions with an enemy token")
    print("as long as there are no more than two of the same kind next")
    print("to each other, or occupying positions 25, 26, 28 and 29.")
    
def getNames():
    print("**************************************************")
    print("****    GREETINGS MORTALS, I AM OSIRIS AND   *****")
    print("****  I WILL BE YOUR GUIDE TO THE AFTERWORLD *****")
    print("****       THOUGH MY POWERS ARE INMENSE,     *****")
    print("****          YOU HAVE BIG SOULS.            *****")
    print("**************************************************")
    print("****  FEAR NOT, FOR I HAVE DIVIDED YOUR SOUL *****")
    print("****     IN FIVE PIECES. YOU\'LL HAVE TO      *****")
    print("****       CROSS THIS VAST UNDEAD LAND       *****")
    print("****     TO GAIN ETERNAL LIFE AT MY SIDE!    *****")
    print("**************************************************")
    print("****       BUT REMEMBER, ALL FIVE PIECES     *****")
    print("****        OF YOUR SOUL HAVE TO CROSS.      *****")
    print("****     THERE CAN BE ONLY ONE AT MY SIDE!   *****")
    print("****                THE LOSER...             *****")
    print("**** SHALL FACE THE ETERNAL WRATH OF ANUBIS! *****")
    print("**************************************************")
    print("HORUS: Both of you, your names! I\'ll chose who goes first!")
    name1 = raw_input("ENTER YOUR NAME: ")
    while(name1 == ""):
        print("HORUS: Speak LOUDER!")
        name1 = raw_input("ONE MORE TIME, ENTER YOUR NAME: ")
    name2 = raw_input("ENTER YOUR NAME: ")
    while(name2 == ""):
        print("HORUS: Speak LOUDER!")
        name2 = raw_input("ONE MORE TIME, ENTER YOUR NAME: ")
    return name1, name2
    
def printBoard(board):
    print(board[0:10])
    print(board[19:9:-1])
    print(board[20:30])

def assignPlayers(name1, name2):
    if int(random.uniform(0, 100)) > 50:
        print("HORUS: " + name1 + " will go first! (You move black tokens)")
        return name1, name1, name2
    else:
        print("HORUS: " + name2 + " will go first! (You move black tokens)")
        return name2, name2, name1

def throwTables():
    wood = int(random.uniform(1, 4))
    black = int(random.uniform(1, 4))
    if black == 4:
        return 6
    else:
        return wood

def turnMessage(player):
    options = ["T", "R", "Y", "t", "r", "y"]
    print("YOUR TURN, " + player +  "!")
    print("Press \'T\' to throw tables")
    print("Press \'R\' to return to main menu")
    print("Press \'Y\' to yield turn")
    choice = raw_input("Your choice: ")
    if choice not in options:
        print("HORUS: Wrong choice!")
        print("YOU HAVE LOST CONTROL OVER YOUR SOULS!")
        return 0
    if choice == "T" or choice == "t":
        return throwTables()
    elif choice == "R" or choice == "r":
        return -1
    elif choice == "Y" or choice == "y":
        return 0
       

def checkswap(board, pos1, pos2):
    if pos2 <= 0:
        return False
    if pos2 == 30:
        return True
    if pos2 >= 24 and board[pos2] != " " and pos2 != 26 and pos2 < 29:
        return False
    else:
        if board[pos2] != " ":
            return (board[pos2] != board[pos2 + 1] and board[pos2] != board[pos2 - 1])
        else:
            return True

def checkFirstRow(token):
    for i in range(0, 10):
        if board[i] == token:
            return False
    return True

def swap(board, pos1, pos2):
    pawn1 = board[pos1]
    pawn2 = board[pos2]
    if not checkswap(board, pos1, pos2):
        print("HORUS: Unable to fulfill request")
        return -1
    else:
        if pos2 == 30:
            token = board[pos1]
            if checkFirstRow(token):
                board[pos1] = " "
            else:
                print("HORUS: This part of your soul can\'t be saved unless you free yours from the first row of the board.")
        elif pos2 < 30:
            if pos2 == 26:
                print("HORUS: You have fallen in the Nile River!")
                for i in range(14,-1,-1):
                    if board[i] == " ":
                        print("Your token returns to the " + i + " position")
                        board[i] = board[pos1]
                        board[pos1] = " "
            elif pawn1 != pawn2:
                board[pos1] = pawn2
                board[pos2] = pawn1
            return 0
        
def initBoard(board):
    for i in range(0, 10):
        if i % 2 == 0:
            board[i] = "W"
        else:
            board[i] = "B"

    board[26] = "R"
    board[30] = "S"
    for i in range(31, 36):
        board[i] = "F"

def showScore(board, name1, name2):
    print("Score: ")
    b_tokens = 5
    w_tokens = 5
    b_count = 0
    w_count = 0
    b_score = 0
    w_score = 0
    for i in range(0, len(board)):
        if board[i] == "B":
            b_count += 1
        if board[i] == "W":    
            w_count += 1
    b_score = b_tokens - b_count
    w_score = w_tokens - w_count
    print(name1 + ": " + str(b_score) + " (Black Tokens)")
    print(name2 + ": " + str(w_score) + " (White Tokens)")
    return b_score, w_score

def changePlayer(player, name1, name2):
    if player == name1:
        player = name2
    else:
        player = name1
    return player

def showAvailableMovements(player):
    options = ["F", "Y", "B", "f", "y", "b"]
    print("HORUS: I have located your soul. What do you want to do now?")
    print("Press \'F\' to move forward")
    print("Press \'B\' to move backwards")
    print("Press \'Y\' to yield turn")
    choice = raw_input("Your choice: ")
    while(choice not in options):
        choice = raw_input("Your choice: ")
    if choice == "F" or choice == "f":
        return 1
    elif choice == "B" or choice == "b":
        return 0
    elif choice == "Y" or choice == "y":
        return -1

def endGame(score1, score2, name1, name2):
    end = False
    if score1 == 5:
        print("OSIRIS: You are the greatest soul, " + name1 + "! Congratulations!")
        print("GAME OVER")
        end = True
    if score2 == 5:
        print("OSIRIS: You are the greatest soul, " + name2 + "! Congratulations!")
        print("GAME OVER")
        end = True
    return end

def menuHandler(choice):
    if choice == "H" or choice == "h":
        printHelp()
        choice = showMenu()
        menuHandler(choice)
    elif choice == "P" or choice == "p":
        name1, name2 = getNames()
        player, name1, name2 = assignPlayers(name1, name2)
        while(1):
            score1, score2 = showScore(board, name1, name2)
            if endGame(score1, score2, name1, name2):
                break
            printBoard(board)
            turn_choice = turnMessage(player)
            if turn_choice == -1:
                jump()
                choice = showMenu()
                menuHandler(choice)
            elif turn_choice == 0:
                player = changePlayer(player, name1, name2)
            else:
                tables = throwTables()
                print("You got " + str(tables) + "!")
                selectSoul(player, name1, name2, board, tables)
                player = changePlayer(player, name1, name2)
    elif choice == "L" or choice == "l":
        pass
    elif choice == "E" or choice == "e":
        print("Thanks for playing!")
        quit()
        
def selectSoul(player, name1, name2, board, tables):
    print("HORUS: Now " + player +  " choose a number from 1 to 30, I\'ll try to locate a piece of your soul there.")
    print("HORUS: Choose wisely, I\'m not as powerful as my father. I cannot give you another chance.")
    number = raw_input("YOUR CHOICE: ")
    try:
        num = int(number)
        real_num = num - 1
        if real_num >= 0 and real_num <= 30:
            if ((player == name1 and board[real_num] == "B") or (player == name2 and board[real_num] == "W")):
                choice = showAvailableMovements(player)
                if choice == 1:
                    swap(board, real_num, real_num + tables)
                elif choice == 0:
                    swap(board, real_num, real_num - tables)
            else:
                print("HORUS: Sorry, I can\'t find a part of your soul there.")
    except:
        print("HORUS: Sorry, I don\'t understand.")
   
initBoard(board)
choice = showMenu()
menuHandler(choice)
    

