class Money(object):
    """Organizes money into dollars and cents"""

    def __init__(self, money):
        self.money = money

    def __str__(self):
        if isinstance(self.money, int):
            return (str(self.money) + ' Cents')
        elif isinstance(self.money, float):
            return ('$ ' + str(self.money))
        elif isinstance(self.money, str):
            return (str(self.money) + " is not a valid amount of money.")


def main():
    money = 5
    cent = Money(money)
    doll = 16.25
    dollar = Money(doll)
    er = "George"
    err = Money(er)
    print(cent)
    print(dollar)
    print(err)

if __name__ == "__main__":
    main()