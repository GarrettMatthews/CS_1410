# Garrett Matthews
# Project 4: Coffee Machine

# I declare that the following source code was written solely by me. I understand that copying any source code,
# in whole or in part, constitutes cheating, and that I will receive a zero on this project if I am found in violation
# of this policy. #

# Importing modules
from product import Product
from cashbox import CashBox
from selector import Selector

# Making the class
class CoffeeMachine (object):
    """"This class runs a coffee machine of 5 options, processing payment, returns, and making of the product"""
    def __init__(self):
        self.product = Product()
        self.cashbox = CashBox()
        self.select = Selector()
        self.spent = 0


    def oneAction(self):
        """The main method, that initializes the deisplay, and receives user input"""
        greeting = "Welcome to Python's Coffee Hub!"
        intro = "PRODUCT LIST: All 35 cents, except bouillon (25 cents)"
        prod_list = "1 = Black, 2 = White, 3 = Sweet, 4 = White & Sweet, 5 = Bouillon"
        samp_comm = "Sample commands: insert 25, select 1. Your command: "
        self.choice = input("{}{}{}{}{}{}{}".format(greeting, '\n', intro, '\n', prod_list, '\n', samp_comm))
        choice_lst = self.choice.split()
        if self.choice in ("quit", "Quit"):
            return False
        elif choice_lst[0] in ('select', 'Select'):
            self.afford(self.choice)
            return True
        elif choice_lst[0] in ('insert', 'Insert'):
            self.cashbox.insert(choice_lst[1])
            return True
        elif self.choice in ("cancel", "Cancel"):
            self.cashbox.returnCoins(self.cashbox.total())
            return True
        elif self.choice in ("total", "Total"):
            total = self.cashbox.total()
            print("{}{}{}".format("You have ", total, " cents left in the machine"))
            return True
        elif self.choice in ("help", "Help"):
            print("{}{}{}{}{}{}{}".format("This machine accepts money and will return coffee or chicken broth.",
                                              '\n', "First INSERT money, then SELECT the product you would like to "
                                                    "have (pick between 1 - 5). To see how much money you've deposited,"
                  "enter Total.",'\n',  "To return your money enter Cancel. To exit this program, enter Quit and you"
                                        " will also see the total that you have spent.", '\n',
                                              "Thank you for using Pythons Coffee Hub! Enjoy your day!"))
            return True
        else:
            print("Command not recognized, try Help for more commands")
            return  True

    def afford(self, select):
        """The method that compares the price of the product requested to the amount of money deposited"""
        self.choice = select
        price = self.select.getPrice(self.choice)
        cash = self.cashbox.total()
        if cash >= price:
            self.select.selector(self.choice)
            self.cashbox.deduct(price)
            self.spent += price
        else:
            print("Sorry, you have not deposited enough money for that")
            print("{}{}".format("Price equals: ", price))
            print("{}{}".format("Money available equals: ", cash))


    def totalCash(self):
        """"Returns the amount of money spent in an interaction"""
        return self.spent


def main():
    m = CoffeeMachine()
    while m.oneAction():
        pass
    total = m.totalCash()
    print(f"Total cash: ${total / 100:.2f}")


if __name__ == "__main__":
    main()