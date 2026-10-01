import pytest

from calculator.calculation import Add, Subtract
from calculator.history import History


def test_empty_history():
    assert History().get_history() == []


def test_mixed_calculations_keep_order():
    history = History()

    first = Add(10, 5)
    second = Subtract(20, 7)

    history.add(first)
    history.add(second)

    assert history.get_history() == [first, second]


def test_returned_history_is_copy():
    history = History()

    calculation = Add(10, 5)
    history.add(calculation)

    copy = history.get_history()
    copy.clear()

    assert history.get_history() == [calculation]


def test_remove_returns_object():
    history = History()

    first = Add(10, 5)
    second = Subtract(20, 7)

    history.add(first)
    history.add(second)

    assert history.remove(0) is first
    assert history.get_history() == [second]

    assert history.remove(0) is second
    assert history.get_history() == []


def test_invalid_removal_preserves_history():
    history = History()

    calculation = Add(10, 5)
    history.add(calculation)

    for index in [-1, 1, 99]:
        with pytest.raises(IndexError):
            history.remove(index)

        assert history.get_history() == [calculation]


def test_histories_are_independent():
    first = History()
    second = History()

    first.add(Add(10, 5))

    assert second.get_history() == []


def test_reject_non_calculation():
    history = History()

    with pytest.raises(TypeError):
        history.add("wrong")

    assert history.get_history() == []


def test_remove_middle():
    history = History()

    first = Add(1, 2)
    middle = Subtract(5, 1)
    last = Add(10, 20)

    history.add(first)
    history.add(middle)
    history.add(last)

    assert history.remove(1) is middle
    assert history.get_history() == [first, last]


def test_remove_from_empty_history():
    history = History()

    with pytest.raises(IndexError):
        history.remove(0)

    assert history.get_history() == []


def test_remove_last():
    history = History()

    first = Add(1, 2)
    middle = Subtract(5, 1)
    last = Add(10, 20)

    history.add(first)
    history.add(middle)
    history.add(last)

    assert history.remove(2) is last
    assert history.get_history() == [first, middle]
