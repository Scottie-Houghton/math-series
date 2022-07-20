from series import fibonacci
from series import lucas
from series import sum_series

def test_fibonacci_index_6():
    actual = fibonacci(6)
    expected = 5
    assert actual == expected