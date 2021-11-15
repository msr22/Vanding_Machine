# All good -to use - new login method

import re

class Item:
    """Class to store & update items in a vending machine"""
    def __init__(self, item_id, price, stock, name):
        self.item_id = item_id
        self.price = price
        self.stock = stock
        self.name = name

    def updateStock(self, stock):
        self.stock = stock

    def buyFromStock(self):         # function to update quantity of items when a purchase is made
        if self.stock == 0:
            print("Item not available")     # if quantity is 0, then display that item is not available
            pass
        else:
            self.stock -= 1         # if a purchase is made successfully, decrease the quantity of item by 1.

class VendingMachine:
    """Class to authenticate login, display vending machine contents & allow purchase"""

    def __init__(self):
        # initialize values
        self.amount = 0
        self.items = []

    def load_vm(self, item):
        self.items.append(item)
    
    def showItems(self):            # function to display items available in the vending machine
        print('\n\tContents of VM\n********************************')
        print('\nItem ID\t\tPrice\tQuantity\tItem Name\n')
        for item in self.items:
            print(item.item_id, '\t\t', '$'+ str(item.price), '\t', item.stock, '\t\t', item.name)


    def addCash(self, money):
        self.amount = self.amount + money

    def buy_item(self, item):
        # if 
        if self.amount < item.price:
            print('You can\'t but this item. Insert more coins.')
        else:
            self.amount -= item.price
            item.buyFromStock()

    def containsItem(self, wanted):     # func to check item availability
        ret = False
        for item in self.items:
            if item.item_id == wanted:
                ret = True
                break
        return ret

    def getItem(self, wanted):          # func to get the item details
        ret = None
        for item in self.items:
            if item.item_id == wanted:
                ret = item
                break
        return ret

    def insertAmountForItem(self, item):    
        # get price of item to be bought
        price = item.price              
        # print the price of item
        self.amount = self.amount + float(input('Please pay: $' + str(price) + ': '))     
        # if full amount is not paid, ask for remaining amount to be paid 
        while self.amount < price:
                self.amount = self.amount + float(input('Remaining amount: $' + str(price - self.amount) + ': '))

    def checkRefund(self):          # func to check if any refund is needed
        if self.amount > 0:
            print('Your change is $' + str(self.amount))
            self.amount = 0

        print('Transaction Complete ...\n')

def login(machine):                 # func to login to the VM
        mach = machine

        # display interface & available items 
        print("\n******************\nNew session...\n******************\n")
        machine.showItems()     
        # Take user ID as input from user    
        print('Please enter your')
        student_id = input('        >MIT Student ID :')

        # Check if the user is present in DB - if yes, take to welcome screen, if no - print invalid id
        file = open("db.txt")
        if(student_id in file.read()):
            print('Hello -', student_id)
            print('\nWelcome to MIT vending machine\n***********************************')
            print('     Student Vending Machine\n***********************************')
            # Ask user what he wants to do
            print('1. Buy\n2. Display items\n3. Quit')
            option = int(input('Your option [1-3]: '))
            return option
        else:
            print('Invalid ID')
            login(mach)
        
def vend():

    machine = VendingMachine()          # Initialize variable with class VendingMachine
    item1 = Item('A1', 10, 2, 'Water')  # Initialize VM with some items.
    item2 = Item('A2', 20, 4, 'Chips')
    item3 = Item('A3', 30, 3, 'Coke')
    item4 = Item('A4', 25, 1, 'Fanta')
    item5 = Item('A5', 35, 4, 'Sprite')
    machine.load_vm(item1)
    machine.load_vm(item2)
    machine.load_vm(item3)
    machine.load_vm(item4)
    machine.load_vm(item5)

    for count in range(0,5):            # Setting count to 5 so that without without rerunning the program, 5 different users can login
        option = login(machine)         # Call login function & get the option from user
        if option == 3:                 # If user choses to Quit, terminate session
            print('Terminating...')
            count += 1
            continue                    # Send back to login screen
        
        continueToBuy = True            # Initialize variable for while loop
        while continueToBuy == True:
            if option == 1:             # User chooses to buy item
                selected = input('Enter Item ID: ')     # Ask user which item he wants to buy for list displayed above
                if machine.containsItem(selected):      # Check if the item is available or not
                    item = machine.getItem(selected)    # If item is available get the item details
                    machine.insertAmountForItem(item)   # get price of item to be bought
                    machine.buy_item(item)              
                    machine.checkRefund()               # If amount entered is more, give additional amount
                    option = int(input('Your option [1-3]: '))  # 1st txn is complete. Ask user what they want to do
                    if option == 3:
                        print('Terminating...') 
                        count += 1
                        continueToBuy = False
                else:
                    print('Item not available. Select another item.')
                
            elif option == 2:
                machine.showItems()
                option = int(input('Your option [1-3]: '))
            
            elif option == 3:
                print('Terminating...')
                count += 1
                continueToBuy = False
            else:
                print('Wrong option')
                continue

                
vend()