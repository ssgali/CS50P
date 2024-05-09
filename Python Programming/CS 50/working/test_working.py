import pytest
from working import convert


def test_convert():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("12:70 AM to 12:60 PM")
    with pytest.raises(ValueError):
        convert("12 AM - 12 PM")
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
