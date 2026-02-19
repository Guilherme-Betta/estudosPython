pieces =    ['wking', 'bking',
            'wqueen', 'bqueen',
            'wpawn', 'bpawn',
            'wrook', 'brook',
            'wbishop', 'bbishop',
            'wknight', 'bknight']   # Peças

rank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # Colunas
file = ['1', '2', '3', '4', '5', '6', '7', '8'] # Fileiras

squares = ['',]

for letter in rank:
    for number in file: # Cria todas as posições que as peças podem ter (corrigir para os bispos na real)
        squares.append((letter+number))

print('Para adicionar uma coordenada, \
digite a letra e o número da coordenada\
(exemplo: a4) e dê Enter.\
Para adicionar peças, digite "b" ou "w" para determinar\
a sua cor (branco e preto respecitvamente)\
e o nome da peça (Exemplo: bking), e dê Enter.\
Quando terminar, basta apertar enter.')  # Estabelece as instruções para criar o tabuleiro

board = {}  # Input das peças no tabuleiro

for i in range(32):
    coordenada = input()
    if coordenada == '':
        break
    peça = input()
    if peça == '':
        break
    board[coordenada] = peça

count = {'wking': 0, 'bking': 0, 'wqueen': 0, 'bqueen': 0, 'wpawn': 0, 'bpawn': 0, 'wrook' : 0, 'brook': 0, 'wbishop': 0, 'bbishop': 0, 'wknight': 0, 'bknight': 0}
for piece in board.values():
    count[piece] = count[piece] + 1

def isValidChessBoard():    # Checador pra ver se é válido
    if coordenada not in squares:
        return False
    elif peça not in pieces:
        return False
    elif count['wking'] != 1:
        return False
    elif count['bking'] != 1:
        return False
    elif count['wpawn'] > 8:
        return False
    elif count['bpawn'] > 8:
        return False
    elif count['wrook'] > 2:
        return False
    elif count['brook'] > 2:
        return False
    elif count['wknight'] > 2:
        return False
    elif count['bknight'] > 2:
        return False
    elif count['wbishop'] > 2:
        return False
    elif count['bbishop'] > 2:
        return False
    elif count['wqueen'] > 9:
       return False
    elif count['bqueen'] > 9:
        return False
    else:
        return True

print(isValidChessBoard())
