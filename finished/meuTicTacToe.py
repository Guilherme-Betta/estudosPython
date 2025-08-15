# Instructions
def ajuda():
    print('Instruções:')
    print('1' + '|' + '2' + '|' + '3')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('7' + '|' + '8' + '|' + '9')
    print('\n')
    print('1 = top-L, 2 = top-M, 3 = top-R' + '\n' +
          '4 = mid-L, 5 = mid-M, 6 = mid-R' + '\n' +
          '7 = low-L, 8 = low-M, 9 = low-R')
    print('Digite "start" para jogar.')


# Game system
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
    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    if board['top-L'] == board['top-M'] == board['top-R'] or \
       board['top-L'] == board['mid-L'] == board['low-L'] or \
       board['mid-L'] == board['mid-M'] == board['mid-R'] or \
       board['low-L'] == board['low-M'] == board['low-R'] or \
       board['top-M'] == board['mid-M'] == board['low-M'] or \
       board['top-R'] == board['mid-R'] == board['low-R'] or \
       board['top-L'] == board['mid-M'] == board['low-R'] or \
       board['top-R'] == board['mid-M'] == board['low-L'] == 'X':
        print('Jogador X ganhou!')
        # break
    elif board['top-L'] == board['top-M'] == board['top-R'] or \
        board['top-L'] == board['mid-L'] == board['low-L'] or \
        board['mid-L'] == board['mid-M'] == board['mid-R'] or \
        board['low-L'] == board['low-M'] == board['low-R'] or \
        board['top-M'] == board['mid-M'] == board['low-M'] or \
        board['top-R'] == board['mid-R'] == board['low-R'] or \
        board['top-L'] == board['mid-M'] == board['low-R'] or \
        board['top-R'] == board['mid-M'] == board['low-L'] == 'O':
        print('Jogador O ganhou!')
        # break
    else:
        print('Deu velha.')
if 'ajuda' == input():
    ajuda()
elif 'start' == input():
    printBoard(theBoard)
