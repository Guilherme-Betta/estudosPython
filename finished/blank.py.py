theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': ' ', 'mid-M': 'X', 'mid-R': 'X',
            'low-L': 'X', 'low-M': 'X', 'low-R': 'O'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)
