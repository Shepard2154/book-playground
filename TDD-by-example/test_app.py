from app import Money, Franc, Money


def test_multiplication():
    five = Money(5)
    assert five * 2 == Money(10)
    assert five * 3 == Money(15)


def test_equality():
    assert Money(5) == Money(5)
    assert Money(5) != Money(6)
    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)
    assert Franc(5) != Money(5)

