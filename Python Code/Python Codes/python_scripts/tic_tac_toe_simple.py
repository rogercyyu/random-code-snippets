theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
i = 0
while i < 9:
    printBoard(theBoard)
    num = int(i)
    print('Turn for ' + turn + '. Move on which space?')
    print('Try number: ' + str(num))
    move = input()
    if move in theBoard:
        theBoard[move] = turn
        i = i + 1
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    else:
        i = i - 1
        if i < 0:
            i = 0
        else:
            print('Incorrect value. Please try again.')
else:
    print('Too many tries.')
        

printBoard(theBoard)
