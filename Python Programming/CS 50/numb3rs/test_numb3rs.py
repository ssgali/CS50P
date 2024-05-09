from numb3rs import validate

def test_validate():
    assert validate("123.123.123.123") == True
    assert validate("cat") == False
    assert validate("266.266.266.266") == False
    assert validate("a.b.c.d") == False
    assert validate("1.0.0.1") == True
    assert validate("0.256.0.1") == False