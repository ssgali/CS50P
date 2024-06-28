from um import count


def test_count():
    assert count("Um") == int(1)
    assert count("Mum") == int(0)
    assert count("Hum, um um hmmm") == int(2)
    assert count("  um   ") == int(1)
