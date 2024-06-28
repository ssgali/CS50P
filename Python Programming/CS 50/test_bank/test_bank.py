from bank import value


def test_for_100():
    assert value("Yo Greetings".strip()) == 100
    assert value("123") == 100
    assert value("Yo whatsapp".strip()) == 100

def test_for_0():
    assert value("Hello there!".strip()) == 0

def test_for_20():
    assert value("hi there.".strip()) == 20