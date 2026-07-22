class Dollar:
    def __init__(self, amount):
        self._amount = amount

    def __mul__(self, multiplier):
        return self._amount * multiplier

    def __eq__(self, other):
        return self._amount == other
