from app import Dollar


def test_multiplication():
    five = Dollar(5)
    assert five * 2 == 10
    assert five * 3 == 15


def test_equality():
    assert Dollar(5) == Dollar(5)
