import um

def test_count():
    assert um.count("um, um, um") == 3
    assert um.count("Hello, um, World") == 1
    assert um.count("Yummy") == 0

def test_numbers_punc():
    assert um.count("123>:.!") == 0

def test_case():
    assert um.count("um, UM") == 2