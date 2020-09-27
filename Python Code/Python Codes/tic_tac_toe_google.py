import random

def plyr1wintest(): #checks if player has 3 in a row
    global winner
    if (1 in plyr1list) and (2 in plyr1list) and (3 in plyr1list) or \
       (4 in plyr1list) and (5 in plyr1list) and (6 in plyr1list) or \
       (7 in plyr1list) and (8 in plyr1list) and (9 in plyr1list) or \
       (1 in plyr1list) and (4 in plyr1list) and (7 in plyr1list) or \
       (2 in plyr1list) and (5 in plyr1list) and (8 in plyr1list) or \
       (3 in plyr1list) and (6 in plyr1list) and (9 in plyr1list) or \
       (1 in plyr1list) and (5 in plyr1list) and (9 in plyr1list) or \
       (3 in plyr1list) and (5 in plyr1list) and (7 in plyr1list):
            print ((name1) + ' wins as X')
            winner = True

def plyr2wintest(): #checks if player has three in a row
    global winner
    if (1 in plyr2list) and (2 in plyr2list) and (3 in plyr2list) or \
       (4 in plyr2list) and (5 in plyr2list) and (6 in plyr2list) or \
       (7 in plyr2list) and (8 in plyr2list) and (9 in plyr2list) or \
       (1 in plyr2list) and (4 in plyr2list) and (7 in plyr2list) or \
       (2 in plyr2list) and (5 in plyr2list) and (8 in plyr2list) or \
       (3 in plyr2list) and (6 in plyr2list) and (9 in plyr2list) or \
       (1 in plyr2list) and (5 in plyr2list) and (9 in plyr2list) or \
       (3 in plyr2list) and (5 in plyr2list) and (7 in plyr2list):
            print ((name2) + ' wins as O')
            winner = True        

def printboard(): #print board
    print(' ')
    print(' '+ position[0] +' | '+ position[1] +' | '+ position[2] + '    ' + '      '+ '1' +' | '+ '2' +' | '+ '3')
    print('-----------' + '        ' + '-----------')
    print(' '+ position[3] +' | '+ position[4] +' | '+ position[5] + '    ' + '      '+ '4' +' | '+ '5' +' | '+ '6')
    print('-----------' + '        ' + '-----------')
    print(' '+ position[6] +' | '+ position[7] +' | '+ position[8] + '    ' + '      '+ '7' +' | '+ '8' +' | '+ '9')
    print(' ')

winner = False #win checker
movecount = 0 #counts amount of turns
playgame = True

print ('welcome to Noughts & Crosses') #title

while playgame == True:
    position = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] #sets the board spaces blank
    plyr1list = []
    plyr2list = []
    gamelist = []

    winner = False
    movecount = 0

    print (' ')
    #Name input
    print ('What is player 1s name?')
    name1 = input()
    print ('thanks '+ (name1) +', Whats player 2s name?')
    name2 = input()
    print ('so '+ (name1) +' is X and '+ (name2) + ' is O')
    input("Press Enter to continue...")

    printboard()

    while (movecount < 9) and (winner == False):

        if (movecount % 2 == 0): #player 1 turn

            print ((name1) + 's ( X ) turn, please choose placement (1-9)')
            move = input()
            if move in ('1', '2', '3', '4', '5', '6', '7', '8', '9') and (int(move) not in (gamelist)):
                plyr1list.append(int(move))
                gamelist.append(int(move))
                print (gamelist) #debug
                position[int(move)-1] = ('X')
                printboard()
                movecount = movecount + 1
                plyr1wintest()
            elif move not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                print ('That is not a valid move! Try again')
            else: print ('That move is taken!, Try again')

        else: #player 2 turn

            print ((name2) + 's ( O ) turn, please choose placement (1-9)')
            move = input()
            if move in ('1', '2', '3', '4', '5', '6', '7', '8', '9') and (int(move) not in (gamelist)):
                plyr2list.append(int(move))
                gamelist.append(int(move))
                print (gamelist) #debug
                position[int(move)-1] = ('O')
                printboard()
                movecount = movecount + 1
                plyr2wintest()
            elif move not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                print ('That is not a valid move! Try again')
            else: print ('That move is taken!, Try again')

    #end game
    if winner == True:
        print ('Congrats!')
    else: print ('Its a tie BOI!')
    print (' ')

    #playagain
    answer = 0
    valid = False
    print ('Would you like to play again (y/n)')
    while valid == False: #waits until valid answer is submitted
        answer = input()
        if answer == 'y':
            print ('aight, resetting...')
            valid = True
        elif answer == 'n':
            print ('aight, cya')
            print (' ') #ASCII art up in here cause why not
            print('             *     ,MMM8&&&.            *')
            print('                  MMMM88&&&&&    .')
            print('                 MMMM88&&&&&&&')
            print('     *           MMM88&&&&&&&&')
            print('                 MMM88&&&&&&&&')
            print('                  MMM88&&&&&&')
            print('                    MMM8&&&      *')
            print('          |\___/| ')
            print('          )     (             .              ')
            print('         =\     /=')
            print('           )===(            Thanks for playing   *')
            print('          /     \ ')
            print('          |     |')
            print('         /       \ ')
            print('         \       / ')
            print('  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_ ')
            print('  |  |  |  |( (  |  |  |  |  |  |  |  |  |  | ')
            print('  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  | ')
            print('  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  | ')
            print('  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ')
            print('  By Me yay|  |  |  |  |  |  |  |  | ')
            valid = True
            playgame = False
        else: print ('answer not valid, please use y or n')
#End
