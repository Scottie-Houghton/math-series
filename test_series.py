from series import fibonacci
from series import lucas
from series import sum_series

def test_fibonacci_index_1():
    actual = fibonacci(1)
    expected = 0
    assert actual == expected

def test_fibonacci_index_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_index_8():
    actual = fibonacci(8)
    expected = 13
    assert actual == expected

def test_lucas_index_1():
    actual = lucas(1)
    expected = 2
    assert actual == expected

def test_lucas_index_2():
    actual = lucas(2)
    expected = 1
    assert actual == expected

def test_lucas_index_7():
    actual = lucas(7)
    expected = 18
    assert actual == expected