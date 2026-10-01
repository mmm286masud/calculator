import pytest

from calculator.calculation import Add, Calculation, Subtract


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


def test_subtract():
    assert Subtract(20, 7).get_result() == 13


def test_subtract_can_return_a_negative_result():
    assert Subtract(5, 10).get_result() == -5


def test_calculation_is_abstract():
    with pytest.raises(TypeError):
        Calculation(10, 5)


def test_polymorphism():
    calculations = [
        Add(10, 5),
        Subtract(20, 7)
    ]

    results = []

    for calculation in calculations:
        results.append(calculation.get_result())

    assert results == [15, 13]


def test_three_calculations_with_one_loop():
    calculations = [
        Add(7, 3),
        Subtract(12, 4),
        Subtract(5, 9)
    ]

    results = []

    for calculation in calculations:
        results.append(calculation.get_result())

    assert results == [10, 8, -4]
