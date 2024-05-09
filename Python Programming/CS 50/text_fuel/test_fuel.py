from fuel import gauge, convert
import pytest


def test_convert():
    assert convert("1/1") == 100
    assert convert("0/100") == 0


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(70) == "70%"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("4/1")
