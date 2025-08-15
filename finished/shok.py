def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)
    print('Enter number (or type "exit" to quit):')
    return input()

print('Enter number:')
number = int(input())

while True:
    x = collatz(number)
    if x == 'exit':
        break
    number = int(x)# Write your code here :-)
