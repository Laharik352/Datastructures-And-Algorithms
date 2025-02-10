import sys
class Customer:
    '''This is a Bank Application. It has a Customer Class with few operations'''
    bankname = 'YESBANK'
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    def deposit(self, amt):
        self.balance = self.balance + amt
        print("The balance after deposit:", self.balance)
    def withdraw(self, amt):
        if amt>self.balance:
            print("Insufficient Balance")
            sys.exit()
        self.balance = self.balance - amt
        print("The balance after withdrawal:", self.balance)
print("Welcome to ", Customer.bankname)
name = input("Enter your name:")
c=Customer(name)
while True:
    print("d-deposit\nw-withdraw\ne-exit")
    option = input("Choose your option: ")
    if option.lower() == "d":
        amount = int(input("Enter the amount to deposit: "))
        c.deposit(amount)
    elif option.lower() == "w":
        amount = int(input("Enter the amount to withdraw: "))
        c.withdraw(amount)
    elif option.lower() == "e":
        print("Thanks for using")
        sys.exit()
    else:
        print("Choose a valid option")
