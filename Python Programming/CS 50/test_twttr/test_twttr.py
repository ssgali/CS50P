from twttr import shorten

def test_shorten_str():
    assert shorten("My name is Ali") == "My nm s l"
    assert shorten("Whts ckng?") == "Whts ckng?"

def test_shorten_digits():
    assert shorten("123") == "123"
    assert shorten("my name is 123") == ("my nm s 123")