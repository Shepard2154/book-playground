class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other

    def __mul__(self, multiplier):
        return self._amount * multiplier


class Dollar(Money):
    pass


class Franc(Money):
    pass
