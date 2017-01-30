class Account():
    __balance = 0

    def deposit(self, amount):
        event = AccountCredited(amount)
        self.__apply_change(event)
        return [event]

    def withdraw(self, amount):
        event = AccountDebited(amount)
        self.__apply_change(event)
        return [event]

    def __apply_change(self, event):
        if isinstance(event, AccountCredited):
            self.__balance += event.amount
            event.balance = self.__balance
        elif isinstance(event, AccountDebited):
            self.__balance -= event.amount
            event.balance = self.__balance


class AccountDebited():

    def __init__(self, amount):
        self.amount = amount


class AccountCredited():

    def __init__(self, amount):
        self.amount = amount
