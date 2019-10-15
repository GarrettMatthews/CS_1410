# Garrett Matthews
# Project 4: Coffee Machine

# I declare that the following source code was written solely by me. I understand that copying any source code,
# in whole or in part, constitutes cheating, and that I will receive a zero on this project if I am found in violation
# of this policy. #

class CashBox (object):
    """Handles all the money of the transaction"""
    def __init__(self):
        self.money = 0
        self.total_spent = 0

    def insert(self, money):
        """Allows for the user to insert money to make a purchase"""
        self.cash = int(money)
        if self.cash % 5 == 0:
            self.money += self.cash
            print("{}{}{}{}{}".format(self.cash," cents inserted.", " You have ", self.money, " cents credit."))
        else:
            print("Invalid amount")
            self.returnCoins(self.cash)


    def returnCoins(self, money):
        """Returns the remaining money"""
        self.cash = money
        if self.cash > 0:
            print("{}{}{}".format("Returning ",self.cash," cents"))
            self.money = 0

    def deduct(self, cost):
        """Charges the amount of the service requested, and returns the change"""
        self.cost = cost
        self.money = self.money - self.cost
        self.returnCoins(self.money)
        self.moneySpent(self.cost)

    def moneySpent(self,money):
        """"Calculates the total money spent"""
        self.spent = money
        self.total_spent += self.spent
        return self.total_spent

    def total(self):
        """Displays the amount of money currently deposited in the machine"""
        return self.money

    def spent(self):
        """Displays the amount of money spent"""
        return self.total_spent


