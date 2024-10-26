# >>> Import modules <<<
# import time
from time import sleep # I am importing just the sleep() function from the <time> library, since that is all I need.
# If you only need a small part of what is in a library, it is better to do it this way, as you load fewer things and,
# thus, use less memory.
import sys
#------------------------------------------------------------------------
# >>> Visual Board Layout <<<
#   X  |  O  |  X
#   -----------------
#   O  |  X  |  O
#   -----------------
#   X  |  O  |  X
#
#------------------------------------------------------------------------
#These are global variables. Since they are defined outside of a function, they can be used anywhere.
b_shouldExitGame = False
b_isFirstMove = True  # This holds whether or not it is the first move of the game.
b_hasEncounteredError = False  # This holds whether or not the code has encountered an error so it can exit if it has
b_foundWinCon = False
i_gameState = 0 # 0 = Main Menu, 1 = Match Setup, 2 = Mid-Match, 3 = Game Over, 4 = Exit Game
i_numMoves = 1 # total number of moves made. Match should end when this reaches 9
i_currentPlayerTurn = 1  # this is whos turn it currently is
i_winner = 0 #Who won? 0 = nobody/tie, 1 = player one, 2 = player 2
s_p1Char = "X" # value for the X player (player 1)
s_p2Char = "O" # value for the O player (Player 2)
s_firstPlayerToGo = "1"  # Which player will go first? defaults to player 1

# these are the values displayed in the squares on the board.
# I am putting a number 1 - 9 in each square that the user will then enter to choose which square they want to play in
# My prefix of ls means a list of strings.
# imo, you should only have 1 data type in a list, as that is how most languages work
#they are ordered weirdly so that the positions on the grid match the number positions on a keybaords Numpad
ls_boardVals = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]


#------------------------------------------------------------------------
# Possible Win Conditions are:
# A1,B1,C1 - Left column                    7,4,1
# A2,B2,C2 - Middle column                  8,5,2
# A3,B3,C3 - Right column                   9,6,3
# A1,A2,A3 - Top row                        7,8,9
# B1,B2,B3 - Middle Row                     4,5,6
# C1,C2,C3 - Bottom Row                     1,2,3
# A1,B2,C3 - Diagonal Top-Left > Btm-Right  7,5,3
# C1,B2,A3 - Diagonal Btm-Left > Top-Right  1,5,9

#------------------------------------------------------------------------
# >>> Define all functions before we use them <<<

# ---- MAIN FUNCTIONS ----

# This is run repeatedly until the program ends via a while loop
def Update():
    #we use the "global" keyword here to tell the script that the variables we use later in the function are the
    # same ones we defined "globally" at the top of the script. Without this, it will think that the variables
    # are local to this function and simply happen to have the same name.
    global i_gameState
    global b_hasEncounteredError

    # call different functions based on where we are in the game (as defined by i_gameState)
    if(b_hasEncounteredError == True):
        return #exit this function
    elif(i_gameState == 0): # Initial Splash Screen
        DrawSplash()
    elif(i_gameState == 1): # Set up menu
        DrawMenus()
    elif(i_gameState == 2): # Mid-Game
        DrawMatch()
    elif(i_gameState == 3): # Game Over
        DrawGameOver()
    elif(i_gameState == 4): #exit the game
        sys.exit()
    else:
        print("ERROR --- ERROR --- ERROR")
        print("INVALID GAME STATE")

# - - - - - - - - - - - - - - - -
# ---- DRAW FUNCTIONS ----
# This clears the output console
# in PyCharm, there is no easy way to do this, so instead I just draw a bunch of empty lines (complain to the devs, lol)
# by assigning a value to <lines> in the (), i gave it a default value and made it an optional argument.
# if I call Clear(), <lines> will be given the value of 50, however, if I put any number in the (), that
# value will be assigned to <lines> instead
# Clear() prints 50 empty lines
# Clear(50) also prints 50 empty lines
# Clear(10) prints 10 empty lines
def Clear(lines = 50):
    for i in range(1,lines):
        print("")

# - - - - - - - - - - - - - - - -
# this draws the splash screen (first screen user sees)
def DrawSplash():
    global i_gameState
    #      #########  #########    #######       #########     ###       #######       #########   #######   #########  ####
    #        ###        ###     ###                ###      ##   ##   ###                ###     ##     ##  ###        ####
    #       ###        ###     ###        ###     ###     ##     ##  ###        ###     ###     ##     ##  #####       ##
    #      ###        ###     ###                ###     #########  ###                ###     ##     ##  ###
    #     ###     #########    #######          ###     ##     ##    #######          ###      #######   #########   ##

    # Draw the animated main menu
    # frame 1
    print("      #########  #########    #######       #########     ###       #######       #########   #######   #########  ####\n\n\n\n\n\n\n\n\n\n\n\n")
    sleep(0.5) # insert a 0.5 second delay before continuing. (Note that I imported the "Time" library at the top of the script. It is not included by default)
    Clear()

    # frame 2
    print(
        "      #########  #########    #######       #########     ###       #######       #########   #######   #########  ####\n"
        "        ###        ###     ###                ###      ##   ##   ###                ###     ##     ##  ###        ####\n\n\n\n\n\n\n\n\n\n\n")
    sleep(0.5)
    Clear()

    # frame 3
    print(
        "      #########  #########    #######       #########     ###       #######       #########   #######   #########  ####\n"
        "        ###        ###     ###                ###      ##   ##   ###                ###     ##     ##  ###        #### \n"
        "       ###        ###     ###        ###     ###     ##     ##  ###        ###     ###     ##     ##  #####       ##\n\n\n\n\n\n\n\n\n\n")
    sleep(0.5)
    Clear()

    # frame 4
    print(
        "      #########  #########    #######       #########     ###       #######       #########   #######   #########  ####\n"
        "        ###        ###     ###                ###      ##   ##   ###                ###     ##     ##  ###        #### \n"
        "       ###        ###     ###        ###     ###     ##     ##  ###        ###     ###     ##     ##  #####       ##   \n"
        "      ###        ###     ###                ###     #########  ###                ###     ##     ##  ###\n\n\n\n\n\n\n\n\n")
    sleep(0.5)
    Clear()

    # frame 5
    print(
        "      #########  #########    #######       #########     ###       #######       #########   #######   #########  ####\n"
        "        ###        ###     ###                ###      ##   ##   ###                ###     ##     ##  ###        #### \n"
        "       ###        ###     ###        ###     ###     ##     ##  ###        ###     ###     ##     ##  #####       ##   \n"
        "      ###        ###     ###                ###     #########  ###                ###     ##     ##  ###               \n"
        "     ###     #########    #######          ###     ##     ##    #######          ###      #######   #########   ##     \n\n\n\n\n\n\n\n")
    sleep(0.75)
    Clear()

    # frame 6
    print("      #########  #########    #######       #########     ###       #######       #########   #######   #########  ####\n"
          "        ###        ###     ###                ###      ##   ##   ###                ###     ##     ##  ###        #### \n"
          "       ###        ###     ###        ###     ###     ##     ##  ###        ###     ###     ##     ##  #####       ##   \n"
          "      ###        ###     ###                ###     #########  ###                ###     ##     ##  ###               \n"
          "     ###     #########    #######          ###     ##     ##    #######          ###      #######   #########   ##     ")
    print("\n"
          "                                          A simple python game example")
    print("\n"
          "\n"
          "   Please choose from the list below: (enter the number, then press enter)\n"
          "   1 = Start New Game (Default Settings)\n"
          "   2 = Start New Game (Set Custom Settings)\n"
          "   3 = Exit Game")

    s_choice = input("Choice: ")
    # react to input (whether valid or not)
    # if we start a new game with default settings
    if(s_choice == "1"):
        i_gameState = 2 # set our game state to the match, so we start a new match upon the start of the next iteration
        return # this would return a value from this function but, since there is no value after it,
        # it simply exits the function early instead (and starts a new iteration of the Update loop)
    elif(s_choice == "2"):
        i_gameState = 1 # set our game state to the set-up screen, so we set up a match on the next iteration
        return
    elif(s_choice == "4"):
        sys.exit() # Exit the script
    else:
        print("ERROR --- INVALID INPUT")
        print("RESTARTING SCRIPT in")
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        Clear(50)
        DrawSplash()

# - - - - - - - - - - - - - - - -
# this draws the set-up match menus
def DrawMenus():
    global i_gameState
    global s_p1Char
    global s_p2Char
    global s_firstPlayerToGo

    Clear()
    # we set the X and O values to nothing, that way their length will not be one. If we left them as is, the code would skip over the while loops below
    s_p1Char = ""
    s_p2Char = ""

    # I am using a While(True)...break construct below to make sure the loop runs at least once.
    # It is equivilent to the do...while control statement you will find in other languages like C, C++, C#, Javascript, etc...
    # The do...while is different from a standard while loop in that the condition is tested after the code runs instead of before.
    # The do...while is typically written as (in C# for example):
    # do
    # {
    #   <run code here>
    # }
    # while(<exit condition>);
    while(True): # this while loop prevents people from choosing nothing, a space, or 2+ characters
        s_p1Char = input("Please choose a single character (no spaces)\n to represent player 1. (The default is a capital X)")
        # the len() function gets the length of whatever is inside it (usually, and in this case, a string)
        if(len(s_p1Char) != 1 or s_p1Char == " "): # we check to make sure the chosen character is valid.
            # if it is not, we tell the user they screwed up, wait 0.5 sec for them to read that
            # and then return back to the start of the loop.
            print("Please choose only ONE, non-space character.")
            sleep(0.5)
        else:
            break

    # now we do the exact same thing as above, except for player 2 and we also check that the P2 character is different from the P1 character
    while(True):
        s_p2Char = input("Please choose a single character (no spaces and different from Player 1)\n to represent player 2. (The default is a capital O)")
        if(len(s_p2Char) != 1 or s_p2Char == " " or s_p2Char == s_p1Char):
            print("Please choose only ONE, non-space character.")
            sleep(0.5)
        else:
            break

    # we use this to have the user decide who will go first
    while(True):
        s_firstPlayerToGo = input("Who will go first? Enter \"1\" or \"2\" and then press enter.")
        if(s_firstPlayerToGo != "1" and s_firstPlayerToGo != "2"):
            print("Please only enter a 1 or a 2.")
            sleep(0.5)
        else:
            break

    i_gameState = 2 #set the gameState to 2 so that we can start the match.
# - - - - - - - - - - - - - - - -

# This draws the screen mid-match
def DrawMatch():
    global b_isFirstMove
    global s_firstPlayerToGo
    global i_currentPlayerTurn
    global b_hasEncounteredError
    global b_foundWinCon
    global i_numMoves
    global ls_boardVals
    global s_p1Char
    global s_p2Char
    global i_gameState

    Clear()

    # draw the board
    print(f" {ls_boardVals[0]}  |  {ls_boardVals[1]}  |  {ls_boardVals[2]}\n"
          f"   -----------------\n"
          f" {ls_boardVals[3]}  |  {ls_boardVals[4]}  |  {ls_boardVals[5]}\n"
          f"   -----------------\n"
          f" {ls_boardVals[6]}  |  {ls_boardVals[7]}  |  {ls_boardVals[8]}\n")

    #set who is going first
    if(b_isFirstMove == True):
        if (s_firstPlayerToGo == "1"):
            i_currentPlayerTurn = 1
            b_isFirstMove = False
        elif(s_firstPlayerToGo == "2"):
            i_currentPlayerTurn = 2
            b_isFirstMove = False
        else:
            print("ERROR - INVALID PLAYER NUMBER!!!")
            b_hasEncounteredError = True;
            return

    print(f"It is player {str(i_currentPlayerTurn)}'s turn!!")
    while (True):
        s_chosenTile = input("Please enter the number of the square you want to play in.\n"
                             "Make sure that square has not already been chosen.")

        #check if input is a valid value
        if(s_chosenTile != "1" and s_chosenTile != "2" and s_chosenTile != "3" and s_chosenTile != "4" and
        s_chosenTile != "5" and s_chosenTile != "6" and s_chosenTile != "7" and s_chosenTile != "8" and s_chosenTile != "9"):
            print("Please insert a number between 1 and 9, inclusive.")
            sleep(1)
            continue
            #take the chosen value, convert it to an int. subtract 1 (because PCs count from 0)
            # and then check that index in the board Vals list to check if the square has already been chosen
        elif(ls_boardVals[int(s_chosenTile) - 1] == s_p1Char or ls_boardVals[int(s_chosenTile) - 1] == s_p2Char):
            print("Please choose a square that has not already been chosen.")
            sleep(1)
            continue
        else: #input is valid and has not already been chosen
            break

    # if it is player 1s turn
    if(i_currentPlayerTurn == 1):
        # set the tile value to the player 1 symbol
        # I have to use this match statement because the tile numbers are out of order relative to the
        # indices of the array. A match statement is basically a stack of if-elif statements that all test
        # the same condition or value, but do different things based on the result. In this case, I am
        # converting the chosen tile number into the correct index for the array.
        # Note, in a lot of other languages, a match statement will be known as a switch statement. They are the same thing.
        # so, below, we are saying: If int(s_chosenTile) == 1, do what is under the "case 1:" statement
        # elif int(s_chosenTile) == 2, do what is in the "case 2:" statement,
        # etc...
        match int(s_chosenTile):
            case 1:
                ls_boardVals[6] = s_p1Char
            case 2:
                ls_boardVals[7] = s_p1Char
            case 3:
                ls_boardVals[8] = s_p1Char
            case 4:
                ls_boardVals[3] = s_p1Char
            case 5:
                ls_boardVals[4] = s_p1Char
            case 6:
                ls_boardVals[5] = s_p1Char
            case 7:
                ls_boardVals[0] = s_p1Char
            case 8:
                ls_boardVals[1] = s_p1Char
            case 9:
                ls_boardVals[2] = s_p1Char
            #below is what is known as a default case. it is what is called if all other conditions are false.
            # it is basically a REQUIRED else statement at the end of the long stack of elif statements
            case _:
                b_hasEncounteredError = True
                print("ERROR: invalid value for s_chosenTile")
                return

        #call the test for win con function, and if one is found, skip to the GameOver function
        if (TestForWinCon() == True):
            i_gameState = 3
        #change it to be player 2s turn
        i_currentPlayerTurn = 2
        #increase the total number of moves by 1
        i_numMoves += 1
    elif(i_currentPlayerTurn == 2):
        # set the tile value to the player 2 symbol
        match int(s_chosenTile):
            case 1:
                ls_boardVals[6] = s_p2Char
            case 2:
                ls_boardVals[7] = s_p2Char
            case 3:
                ls_boardVals[8] = s_p2Char
            case 4:
                ls_boardVals[3] = s_p2Char
            case 5:
                ls_boardVals[4] = s_p2Char
            case 6:
                ls_boardVals[5] = s_p2Char
            case 7:
                ls_boardVals[0] = s_p2Char
            case 8:
                ls_boardVals[1] = s_p2Char
            case 9:
                ls_boardVals[2] = s_p2Char
            # below is what is known as a default case. it is what is called if all other conditions are false.
            # it is basically a REQUIRED else statement at the end of the long stack of elif statements
            case _:
                b_hasEncounteredError = True
                print("ERROR: invalid value for s_chosenTile")
                return

        #call the test for win con function, and if one is found, skip to the GameOver function
        if(TestForWinCon() == True):
            i_gameState = 3
        # change it to be player 1s turn
        i_currentPlayerTurn = 1
        # increase the total number of moves by 1
        i_numMoves += 1
    else: #i_currentPlayerTurn is an invalid number
        print("ERROR --- ERROR --- ERROR")
        print("Invalid value for i_currentPlayerTurn")
        b_hasEncounteredError = True
        sleep(1)
        return

# - - - - - - - - - - - - - - - -
# this draws the screen for after the game ends
def DrawGameOver():
    global i_winner
    global i_gameState
    global s_p1Char
    global s_p2Char
    global b_hasEncounteredError
    i_gameState = 4

    Clear()
    if(i_winner == 0):
        print("Game Complete!!\nIt was a TIE!!!\n\n(Please restart the program to play again!!)\n")
        print("Thanks for playing")
        print("\n\n(Game Closing in 15 sec...)")
        sleep(5)
        Clear()
        print("Game Complete!!\nIt was a TIE!!!\n\n(Please restart the program to play again!!)\n")
        print("Thanks for playing")
        print("\n\n(Game Closing in 10 sec...)")
        sleep(5)
        Clear()
        print("Game Complete!!\nIt was a TIE!!!\n\n(Please restart the program to play again!!)\n")
        print("Thanks for playing")
        print("\n\n(Game Closing in 5 sec...)")
        sleep(5)
    elif(i_winner == 1):
        print(f"Game Complete!!\nPLAYER 1 ({s_p1Char}) WON!!!\n\n(Please restart the program to play again!!)\n")
        print("Thanks for playing")
        print("\n\n(Game Closing in 15 sec...)")
        sleep(5)
        Clear()
        print(f"Game Complete!!\nPLAYER 1 ({s_p1Char}) WON!!!\n\n(Please restart the program to play again!!)\n")
        print("Thanks for playing")
        print("\n\n(Game Closing in 10 sec...)")
        sleep(5)
        Clear()
        print(f"Game Complete!!\nPLAYER 1 ({s_p1Char}) WON!!!\n\n(Please restart the program to play again!!)\n")
        print("Thanks for playing")
        print("\n\n(Game Closing in 5 sec...)")
        sleep(5)
    elif (i_winner == 2):
        print(f"Game Complete!!\nPLAYER 2 ({s_p2Char}) WON!!!\n\n(Please restart the program to play again!!)\n")
        print("Thanks for playing")
        print("\n\n(Game Closing in 15 sec...)")
        sleep(5)
        Clear()
        print(f"Game Complete!!\nPLAYER 2 ({s_p2Char}) WON!!!\n\n(Please restart the program to play again!!)\n")
        print("Thanks for playing")
        print("\n\n(Game Closing in 10 sec...)")
        sleep(5)
        Clear()
        print(f"Game Complete!!\nPLAYER 2 ({s_p2Char}) WON!!!\n\n(Please restart the program to play again!!)\n")
        print("Thanks for playing")
        print("\n\n(Game Closing in 5 sec...)")
        sleep(5)
    else:
        b_hasEncounteredError = True
        return

# ---- OTHER FUNCTIONS ----
# this tests to see if the board contains a win condition
def TestForWinCon():
    global i_winner
    global i_numMoves
    global i_gameState
    # Possible Win Conditions are:
    # A1,B1,C1 - Left column                    1,4,7 - 1
    # A2,B2,C2 - Middle column                  2,5,8 - 1
    # A3,B3,C3 - Right column                   3,6,9 - 1
    # A1,A2,A3 - Top row                        1,2,3 - 1
    # B1,B2,B3 - Middle Row                     4,5,6 - 1
    # C1,C2,C3 - Bottom Row                     7,8,9 - 1
    # A1,B2,C3 - Diagonal Top-Left > Btm-Right  1,5,9 - 1
    # C1,B2,A3 - Diagonal Btm-Left > Top-Right  7,5,3 - 1

    #actually test if there is a win condition

    #check if there was a tie
    if(i_numMoves >= 9):
        i_winner = 0
        i_gameState = 3
        return True
    #test if there is a player 1 win
    elif((ls_boardVals[0] == ls_boardVals[3] == ls_boardVals[6] == s_p1Char) or
    (ls_boardVals[1] == ls_boardVals[4] == ls_boardVals[7] == s_p1Char) or
    (ls_boardVals[2] == ls_boardVals[5] == ls_boardVals[8] == s_p1Char) or
    (ls_boardVals[0] == ls_boardVals[1] == ls_boardVals[2] == s_p1Char) or
    (ls_boardVals[3] == ls_boardVals[4] == ls_boardVals[5] == s_p1Char) or
    (ls_boardVals[6] == ls_boardVals[7] == ls_boardVals[8] == s_p1Char) or
    (ls_boardVals[0] == ls_boardVals[4] == ls_boardVals[8] == s_p1Char) or
    (ls_boardVals[6] == ls_boardVals[4] == ls_boardVals[2] == s_p1Char)):
        i_winner = 1
        i_gameState = 3
        return True

    #else, test for player 2 win
    elif((ls_boardVals[0] == ls_boardVals[3] == ls_boardVals[6] == s_p2Char) or
    (ls_boardVals[1] == ls_boardVals[4] == ls_boardVals[7] == s_p2Char) or
    (ls_boardVals[2] == ls_boardVals[5] == ls_boardVals[8] == s_p2Char) or
    (ls_boardVals[0] == ls_boardVals[1] == ls_boardVals[2] == s_p2Char) or
    (ls_boardVals[3] == ls_boardVals[4] == ls_boardVals[5] == s_p2Char) or
    (ls_boardVals[6] == ls_boardVals[7] == ls_boardVals[8] == s_p2Char) or
    (ls_boardVals[0] == ls_boardVals[4] == ls_boardVals[8] == s_p2Char) or
    (ls_boardVals[6] == ls_boardVals[4] == ls_boardVals[2] == s_p2Char)):
        i_winner = 2
        i_gameState = 3
        return True

        # in this case, we actually are returning a value. Notice that, in the DrawMatch function
        # there is a variable set with an = before this function call. (near lines 292 and 301) That variable will be set to
        # this value returned below

        # if there is no win, return False
    else:
        return False


#---------------------------------------------------------------------------
# >>>>> ACTUALLY RUN THE GAME <<<<<
i_iter = 0
while(b_shouldExitGame == False):
    Update()
    if(b_hasEncounteredError == True):
        print("ERROR --- ERROR --- ERROR")
        print("Program exiting in 5 seconds...")
        sleep(5)
        break #exit this loop and, since there is no code below this loop, exit the program

    # error catching to prevent infinite loop
    # if, for some reason, we have looped 100 times, exit.
    if(i_iter == 100):
        i_gameState = 3
        print(f"ERROR - MAX GAME LOOP ITERATIONS REACHED ({i_iter})")
        break;
    else: # otherwise, add 1 to the number of iterations
        i_iter += 1
# end of program