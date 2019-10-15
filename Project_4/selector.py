# Garrett Matthews
# Project 4: Coffee Machine

# I declare that the following source code was written solely by me. I understand that copying any source code,
# in whole or in part, constitutes cheating, and that I will receive a zero on this project if I am found in violation
# of this policy. #

# Importing modules
from product import Product
from cashbox import CashBox

class Selector (object):
    """Class that selects the product requested"""
    def __init__(self):
        self.product = Product()
        self.cashbox = CashBox()

    def getPrice(self, option):
        """Returns the price of the requested product"""
        self.option = option
        options = self.option.split()
        if options[1] in ('1','2','3','4'):
            return 35
        elif options[1] in ('5'):
            return 25

    def selector(self, select):
        """Retrieves the recipe and runs the creation of the product"""
        self.select = select
        self.product.coffee(self.select)


