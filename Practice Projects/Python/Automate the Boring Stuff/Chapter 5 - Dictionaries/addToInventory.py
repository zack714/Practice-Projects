"""
This program is an addenum to the previous fantasy inventory program.
We're going to update it so that we can add loot to our inventory.
"""

def addToInventory(inventory, addedItems):
    
    #create a dict to store what the new items are and how many of each there is.
    newItems = {}
    for item in addedItems:
        newItems.setdefault(item,0)
        newItems[item]+=1
    
    #now loop through newItems, and compare it to the inventory and add quantities 
    for k,v in newItems.items():
        inventory.setdefault(k,0)
        inventory[k]+=v

    #return the updated inventory.
    return inventory

#from the previous project
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(inventory[k])+" "+k)
        item_total+=v
    
    print("Total number of items: " + str(item_total))
    
    



inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)