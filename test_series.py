from series import fibonacci
from series import lucas
from series import sum_series

def test_fibonacci_index_6():
    actual = fibonacci(6)
    expected = 5
    assert actual == expected

def test_fibonacci_index_7():
    actual = fibonacci(7)
    expected = 8
    assert actual == expected

def test_fibonacci_index_8():
    actual = fibonacci(8)
    expected = 13
    assert actual == expected

def test_lucas_index_5():
    actual = lucas(5)
    expected = 7
    assert actual == expected

def test_lucas_index_6():
    actual = lucas(6)
    expected = 11
    assert actual == expected

def test_lucas_index_7():
    actual = lucas(7)
    expected = 18
    assert actual == expected