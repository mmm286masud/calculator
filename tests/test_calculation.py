from calculator.calculation import Add


def test_add_10_and_5():
    calculation = Add(10, 5)
    result = calculation.get_result()
    assert result == 15


def test_add_100_and_50():
    calculation = Add(100, 50)
    result = calculation.get_result()
    assert result == 150


def test_add_zero_and_five():
    calculation = Add(0, 5)
    result = calculation.get_result()
    assert result == 5


def test_add_negative_numbers():
    calculation = Add(-10, -5)
    result = calculation.get_result()
    assert result == -15
