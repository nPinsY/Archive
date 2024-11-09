import numb3rs

def test_numbers():
    assert numb3rs.validate("0.50.170.255") == True
    assert numb3rs.validate("119.119.119.119") == True
    assert numb3rs.validate("0.50.170.256") == False
    assert numb3rs.validate("256.170.50.0") == False

def test_alpha():
    assert numb3rs.validate("Hello.0.0.World") == False
    assert numb3rs.validate("Hello, World") == False

def test_format():
    assert numb3rs.validate("0.0.0") == False
    assert numb3rs.validate("123456789") == False
    assert numb3rs.validate("....") == False