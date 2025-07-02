"""
This program is to display the quantities of various contents of a user's inventory,
which will be represented with a dictionary.
"""
import pprint

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(inventory[k])+" "+k)
        item_total+=v
    
    print("Total number of items: " + str(item_total))
displayInventory(stuff)
