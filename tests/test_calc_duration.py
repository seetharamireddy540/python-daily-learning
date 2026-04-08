import pytest
from calc_duration import calc_duration


def test_example_1_minimum():
    result = calc_duration(93784.5165416, stretch=False)
    assert result == "1 day, 2 hours, 3 minutes, 4 seconds"


def test_example_1_stretch():
    result = calc_duration(93784.5165416, stretch=True)
    assert result == "1 day, 2 hours, 3 minutes, 4 seconds, 516 ms, 541 us, 600 ns"


def test_example_2_minimum():
    result = calc_duration(300.721000605, stretch=False)
    assert result == "5 minutes"


def test_example_2_stretch():
    result = calc_duration(300.721000605, stretch=True)
    assert result == "5 minutes, 721 ms, 605 ns"


def test_zero():
    assert calc_duration(0) == "0 seconds"


def test_plural_handling():
    assert calc_duration(86400) == "1 day"
    assert calc_duration(172800) == "2 days"
    assert calc_duration(3600) == "1 hour"
    assert calc_duration(7200) == "2 hours"
    assert calc_duration(60) == "1 minute"
    assert calc_duration(120) == "2 minutes"
    assert calc_duration(1) == "1 second"
    assert calc_duration(2) == "2 seconds"
