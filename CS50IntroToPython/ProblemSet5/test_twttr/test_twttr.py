from twttr import shorten

def test_lower():
    assert shorten("aqwe") == "qw"

def test_upper():
    assert shorten("AQWE") == "QW"

def test_punc():
    assert shorten("d.e.d") == "d..d"

def test_number():
    assert shorten("abc123") == "bc123"