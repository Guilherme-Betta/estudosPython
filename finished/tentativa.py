age = ''
print('Please, type your name.')
name = input()
if name == 'Alice':
    print('Hello, Alice.')
elif age == '':
    print('Please, type your age.')
    age = int(input())
    if age <= 12:
        print('You are not Alice, kiddo.')
    elif age >= 1000:
        print('You are not Alice, immortal vampire.')
    elif age >= 100:
        print('You are not Alice, granny.')
    else:
        print('Ok then.')

