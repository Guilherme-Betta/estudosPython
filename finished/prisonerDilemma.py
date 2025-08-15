# Prisoner`s dilemma tentativa

import random

# Regras

scorePlayer1 = 0        ## Pontuações no começo do jogo
scorePlayer2 = 0

if player1:
    otherPlayer = player2
elif player2:
    otherPlayer = player1

move = [cooperate, defect]      ## Opções de jogada

rounds = []       ## Número de rodadas

for i in range(0 , 200):
    rounds.append(i)

if rounds[0]:
    move = firstMove
elif rounds[1:200]:
    move = nextMove


def cooperate():
    if movePlayer2 == cooperate:
        scorePlayer1 += 3
        scorePlayer2 += 3
    elif movePlayer2 == defect:
        scorePlayer2 += 5
def defect():
    if movePlayer2 == cooperate:
        scorePlayer1 += 5
    elif movePlayer2 == defect:
        scorePlayer1 += 0


# Andamento do jogo?

if movePlayer1 == cooperate:
    cooperate()
elif movePlayer2 == defect:
    defect()

# Estratégias

strategy = [titForTat, defecter, random]

# random

firstMove = move[int(random.randint(0,1))]
nextMove = move[int(random.randint(0,1)))]

# titForTat

firstMove = cooperate()
nextMove = moveOtherPlayer

# defecter

firstMove = defect()
nextMove = defect()

# Primeira rodada

if rounds[0]:
    movePlayer1 = firstMove
    movePlayer2 = firstMove
    rounds[1]

# Rodada

def rounds():
    movePlayer1()
    movePlayer2()

