string = input()

def reverseString():
    letters = []
    length = len(string)
    for i in range(length):
        letters.insert(i, string[length - 1])
        length = length - 1
    reverseString = ''.join(letters)
    print(reverseString)

reverseString()
