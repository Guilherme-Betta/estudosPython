spam = ["apples", "bananas", "tofu", "cats"]
cookie = []


def commaCode(list):
    if len(list) == 0:
        print('.')
    else:
        for i in range(len(list) - 1):
            print(list[i] + ", ", end="")
        print(end="" + "and " + list[-1] + ".")

commaCode(cookie)
