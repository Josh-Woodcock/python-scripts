import pprint

def displayInventory(inventory):
    
    itemNumber = 0
    print('Inventory -')

    for k, v in inventory.items():
        print((str(v) + ' ' + k))
        itemNumber += v
    print('Total number of items - ' + str(itemNumber))


def addToInventory(inventory, addedItems):
    
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)


inventory = {'rope': 1,'torch': 6, 'gold coin': 42, 'dagger': 1,'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(inventory)
addToInventory(inventory, dragonLoot)
displayInventory(inventory)
