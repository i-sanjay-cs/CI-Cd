# test_my_application.py
from my_application import add, subtract

def test_addition():
    assert add(3, 4) == 7

def test_subtraction():
    assert subtract(7, 3) == 4

def test_subtraction():
    assert subtract(2, 3) == 4
    
def test_addition():
    assert add(3, 4) == 10