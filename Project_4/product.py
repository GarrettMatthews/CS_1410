# Garrett Matthews
# Project 4: Coffee Machine

# I declare that the following source code was written solely by me. I understand that copying any source code,
# in whole or in part, constitutes cheating, and that I will receive a zero on this project if I am found in violation
# of this policy. #

# Importing modules

from cashbox import CashBox

class Product (object):
    """The class that holds the recipe and returns the instructions for making the product"""
    def __init__(self):
        self.cashbox = CashBox()

    def coffee(self, choice):
        """Assembles the requested product"""
        self.choice = choice
        cup = "Dispensing cup"
        coffee = "Dispensing coffee"
        water = "Dispensing water"
        cream = "Dispensing creamer"
        sugar = "Dispensing sugar"
        bouillon = "Dispensing bouillon powder"
        if self.choice in ("select 1", "Select 1"):
            black = "Making black:"
            formula = ("{}{}{}{}{}{}{}{}{}{}".format(black, '\n', '\t', cup, '\n', '\t', coffee, '\n', '\t', water))
            print(formula)
        elif self.choice in ("select 2", "Select 2"):
            white = "Making white:"
            formula = ("{}{}{}{}{}{}{}{}{}{}{}{}{}".format(white, '\n', '\t', cup, '\n', '\t', coffee, '\n', '\t',
                                                           cream, '\n', '\t', water))
            print(formula)
        elif self.choice in ("select 3", "Select 3"):
            sweet = "Making sweet:"
            formula = ("{}{}{}{}{}{}{}{}{}{}{}{}{}".format(sweet, '\n', '\t', cup, '\n', '\t', coffee,
                                                           '\n', '\t', sugar, '\n', '\t', water))
            print(formula)
        elif self.choice in ("select 4", "Select 4"):
                white_sweet = "Making white sweet:"
                formula =  (white_sweet, '\n', '\t', cup, '\n', '\t', coffee, '\n', '\t', cream, '\n', '\t', sugar,
                            '\n', '\t',water)
                print(formula)
        elif self.choice in ("select 5", "Select 5"):
            chxn = "Making bouillon"
            formula = ("{}{}{}{}{}{}{}{}{}{}".format(chxn, '\n', '\t', cup, '\n', '\t', bouillon, '\n', '\t', water))
            print(formula)
        else:
            formula = ("Invalid selection")
            print(formula)
