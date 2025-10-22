import pytest
from utils.math import add


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5


def test_add_mixed():
    assert add(-5, 10) == 5