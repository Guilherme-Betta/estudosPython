while True:
    print('Who are you?')
    name = input('Insert name: ')
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input('Insert password: ')
    if password == 'swordfish':
        break
print('Access granted.')
