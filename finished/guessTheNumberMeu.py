import random
num = random.randint(1 , 20)
print('I am thinking of a number between 1 and 20.')
print('Take a guess')
guess = ''
while guess != num:
    guess = int(input())
    if guess < num:
        print('Your guess is too low.')
    elif guess > num:
        print('Your guess is too high.')
    else:
        print('Nice.')

