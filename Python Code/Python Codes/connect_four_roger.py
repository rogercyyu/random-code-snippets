# Connect 4 game.
# 6 rows by 7 columns.
# Winning when 4 in a row connected.

# Use grids.
# Win condition?
# AI? Or two player?

import sys
import random

theBoard = {'A1':1, 'B1':2, 'C1':3, 'D1':4, 'E1':5, 'F1':6, 'G1':7,
          'A2':8, 'B2':9, 'C2':10, 'D2':11, 'E2':12, 'F2':13, 'G2':14,
          'A3':15, 'B3':16, 'C3':17, 'D3':18, 'E3':19, 'F3':20, 'G3':21,
          'A4':22, 'B4':23, 'C4':24, 'D4':25, 'E4':26, 'F4':27, 'G4':28,
          'A5':29, 'B5':30, 'C5':31, 'D5':32, 'E5':33, 'F5':34, 'G5':35,
          'A6':36, 'B6':37, 'C6':38, 'D6':39, 'E6':40, 'F6':41, 'G6':42,
          '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7}

inverted_theBoard = dict([[v,k] for k,v in theBoard.items()])

# grid {keys:values}.
def Play():
    position = [' ' for _ in range(42)]
    movecount = 0
    print ('Welcome to the game of connect-four!')
    while True:
        print('Do you want to play against the computer (y/n)?')
        choice = input()
        if choice in ('y', 'n'):
            break
    if choice == 'n':
        print ('You have chosen to play against another friend.')
        print ('The first player to go will be X.')
        print ('Press ENTER to continue:')
        input()
        printBoard(position)
        players = [('X'), ('O')]
        while movecount < 42:
            while True:
                player = players[movecount % 2]
                print ("It is player %s's turn." % player)
                print ('Please choose placement by using coordinates (e.g A6) or number (1-7):')
                x = input().upper() # ask user to enter coordinates.
                if x in theBoard.keys(): # check if user input is valid.
                    move = theBoard[x]
                    while True:
                        if position[move - 1] != ' ':
                            break
                        else:
                            try: 
                                while position[move + 6] == ' ': # gravity
                                    move += 7
                            except (IndexError):
                                pass
                            position[move - 1] = player[0] # update board.
                            printBoard(position)
                            movecount += 1
                            print ('Movecount: %s.' % movecount)
                        if winConditions(position, player):
                            print ('The WINNNER is player %s. Congrats!' % player)
                            return
                elif x == 'Q':
                    return
                else:
                    printBoard(position)
                    print ('Invalid input, please try again.')
                    print ('Movecount: %s.' % movecount)
                    continue
        else:
            print ('It is a tie!')
    else:
        print ('You have chosen to play against the computer')
        while True:
            print('Do you want to be X or O (x,o)?')
            choice = input()
            if choice in ('x', 'o'):
                break
        if choice == 'x':
            player = 'X'
            computer = 'O'
        else:
            player = 'O'
            computer = 'X'
        if random.randint(0, 1) == 1:
            first = 'player'
        else:
            first = 'computer'
        print ('You have chosen to be %s and the %s will go first.' % (player, first))
        movecount = 0
        if first == 'player':
            players = [player, computer]
            turn = 'player'
        else:
            players = [computer, player]
            turn = 'computer'
        while movecount < 42:
            while True:
                player = players[movecount % 2]
                printBoard(position)
                print ("It is the %s's turn." % turn)
                if turn == 'player':
                    print ('Please choose placement by using coordinates (e.g A6) or number (1-7):')
                    x = input().upper()
                    turn = 'computer'
                else:
                    x = computerTurn(position, player)
                    turn = 'player'
                if x in theBoard.keys(): # check if user input is valid.
                    move = theBoard[x]
                    while True:
                        if position[move - 1] != ' ':
                            break
                        else:
                            try: 
                                while position[move + 6] == ' ': # gravity
                                    move += 7
                            except (IndexError):
                                pass
                            position[move - 1] = player[0] # update board.
                            printBoard(position)
                            movecount += 1
                            print ('Movecount: %s.' % movecount)
                        if winConditions(position, player):
                            print ('The WINNNER is player %s. Congrats!' % player)
                            return
                elif x == 'Q':
                    return
                else:
                    printBoard(position)
                    print ('Invalid input, please try again.')
                    print ('Movecount: %s.' % movecount)
                    continue
                        
        else:
            print('It is a tie!')
                
def computerTurn(position, player):
    for x in range(42):
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        try:
            if position[x] == player and position[x + 1] == player and position[x + 2] == player: # check horizontal spaces
                if x > 39:
                    x = x - 3
                x = inverted_theBoard[x + 3]
                print ('horizontal')
                return x
            elif position[x] == player and position[x + 7] == player and position[x + 14] == player: # check vertical spaces
                if x > 21:
                    x = x - 21
                x = inverted_theBoard[x + 21]
                print ('vertical')
                return x
            elif position[x] == player and position[x + 6] == player and position[x + 12] == player: # check / spaces
                if x > 24:
                    x = x - 18
                x = inverted_theBoard[x + 18]
                print ('/')
                return x
            elif position[x] == player and position[x + 8] == player and position[x + 16] == player: # check \ spaces
                if x > 18:
                    x = x - 24
                x = inverted_theBoard[x + 24]
                print ('\\')
                return x
        except (IndexError):
            break
    x = str (random.randint(1, 7))
    print ('random')
    return x
                

# Win conditions.
def winConditions(position, player):
    for x in range(42):
        try:
            if position[x] == player and position[x + 1] == player  and position[x + 2] == player  and position[x + 3] == player: # check horizontal spaces
                return True
            if position[x] == player and position[x + 7] == player  and position[x + 14] == player  and position[x + 21] == player: # check vertical spaces
                return True
            if position[x] == player and position[x + 6] == player  and position[x + 12] == player  and position[x + 18] == player: # check / spaces
                return True
            if position[x] == player and position[x + 8] == player  and position[x + 16] == player  and position[x + 24] == player: # check \ spaces
                return True
        except (IndexError):
            return False


# print board.
def printBoard(position):
    print ('''
    -----------------------------
  1 | %s | %s | %s | %s | %s | %s | %s |
    -----------------------------        
  2 | %s | %s | %s | %s | %s | %s | %s |
    -----------------------------
  3 | %s | %s | %s | %s | %s | %s | %s |
    -----------------------------
  4 | %s | %s | %s | %s | %s | %s | %s |
    -----------------------------
  5 | %s | %s | %s | %s | %s | %s | %s |
    -----------------------------
  6 | %s | %s | %s | %s | %s | %s | %s |
    -----------------------------
      A   B   C   D   E   F   G
     (1) (2) (3) (4) (5) (6) (7)
    ''' % tuple (p for p in position))
           
while True:
    Play()
    while True:
        print ('Would you like to play again (y/n)?')
        answer = input()
        if answer in ('y', 'n'):
            break
    if answer == 'n':
        break
    print ('Restarting')
print ('Good bye.')
        
