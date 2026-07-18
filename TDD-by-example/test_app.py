from app import Dollar


def test_multiplication():
    five = Dollar(5)
    assert five * 2 == 10
