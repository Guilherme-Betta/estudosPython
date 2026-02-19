import pprint

def displayInventory():
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        item_total = int(item_total) + int(v)
        print(str(v) + ' ' + str(k))
    print('Total number of items: ' + str(item_total))

inventory = {}

while True:
    item = input()
    if item == '':
        break
    n = input()
    if n == '':
        n = 1
        break
    inventory[item] = n

displayInventory()
