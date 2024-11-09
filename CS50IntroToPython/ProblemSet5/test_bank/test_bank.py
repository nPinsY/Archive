from bank import value

def test_0():
    assert value("hello") == 0
    assert value("  hello  ") == 0
    assert value("HeLLo") == 0

def test_20():
    assert value("hi") == 20
    assert value("howdy") == 20
    assert value("h") == 20

def test_100():
    assert value("bonjour") == 100
    assert value("goodbye") == 100