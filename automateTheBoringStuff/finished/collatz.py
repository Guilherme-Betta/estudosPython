import sys
exit = quit = 0
def collatz(n):
    while True:
        if n == 1:
            break
        elif n % 2 == 1:
            n = 3 * n + 1
        elif n % 2 == 0:
            n = n / 2
        print(n)


while True:
    n = int(input('Enter number:'))
    if n == 0:
        sys.exit
    else:
        collatz(n)
