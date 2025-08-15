import random

def test():
    flips = []

    heads = 0
    tails = 1

    numberOfStreaks = 0
    x = 0

    numOfFlips = int(input('Enter the number of flips to be made: '))
    for i in range(int(numOfFlips)):
        flip = random.randint(0 , 1)
        if flip == heads:
            print('H', end='')
        elif flip == tails:
            print('T', end='')
        flips.append(flip)
        while x <= len(flips) - 6:
            if flips[x] == flips[x + 1] == flips[x + 2] == flips[x + 3] == flips[x + 4] == flips[x + 5]:
                numberOfStreaks += 1
                x += 6
            else:
                x += 1
    print(flips)
    print(numberOfStreaks)
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))

test()
