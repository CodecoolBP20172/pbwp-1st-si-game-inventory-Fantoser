# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification
import csv


# Displays the inventory.
def display_inventory(inventory):
    amount = 0
    print("Inventory:")
    for key in inventory:
        print(str(inventory[key]) + " " + key)
        amount += inventory[key]

    print("Total number of items: " + str(amount))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i not in inventory:
            inventory.update({i:0})
        for key in inventory:
            if i == key:
                inventory[key] += 1


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    alist = ()
    if order != None:
        alist = sorted([(value,key) for (key,value) in inv.items()])
    if order == "desc":
        alist.reverse()
    print("Inventory:")
    print("  count    item name")
    print("---------------------")
    if order != None:
        for key in alist:
            print("%5s %15s" % (key[0],key[1]))
    if order == None:
        display_inventory(inventory)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    implist = []
    with open(filename) as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        for row in readcsv:
            for item in row:
                implist.append(item)
    add_to_inventory(inventory, implist)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    exlist = []
    for i in list(inventory.items()):
        for j in range(i[1]):
            exlist.append(i[0])
    with open(filename, 'wt') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerow(exlist)
