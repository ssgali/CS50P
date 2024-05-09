from plates import is_valid

def test_is_valid():
    assert is_valid("AAA222") == True
    assert is_valid("50AB50") == False
    assert is_valid("AAAAAAAAA") == False

def test_for_non_strings():
    assert is_valid("CS50C") == False
    assert is_valid("CS@#50") == False

def test_for_strings():
    assert is_valid("ABCDEF") == True
    assert is_valid("abc ,50") == False

def test_for_numbers():
    assert is_valid("909090") == False
    assert is_valid("abc05") == False
    assert is_valid("0000") == False
