class Money:
    _amount = None

    def __eq__(self, other):
        return self._amount == other


class Dollar(Money):
    def __init__(self, amount):
        self._amount = amount

    def __mul__(self, multiplier):
        return self._amount * multiplier


class Franc(Money):
    def __init__(self, amount):
        self._amount = amount

    def __mul__(self, multiplier):
        return self._amount * multiplier

