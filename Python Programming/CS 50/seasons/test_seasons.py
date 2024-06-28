from seasons import check
import pytest
import sys

def test_check():
    assert check("2021-12-12") == ["2021","12","12"]
    with pytest.raises(SystemExit):
        check("abcd")
