import pytest
from app.calculator import addition, subtraction, multiplication, division

def test_add():
    assert addition(3, 5) == 8

def test_add_negative_numbers():
    assert addition(-2, 3) == 1
    assert addition(-2, -3) == -5    

def test_subtract():
    assert subtraction(10, 2) == 8
    

def test_subtract_negative_numbers():
    assert subtraction(-5, 3) == -8
    assert subtraction(-5, -3) == -2


def test_multiply():
    assert multiplication(3, 7) == 21
    

def test_multiply_negative_numbers():
    assert multiplication(-3, 7) == -21
    assert multiplication(-3, -7) == 21

def test_divide():
    assert division(4, 2) == 2
    
def test_divide_negative_numbers():
    assert division(-8, 2) == -4
    assert division(-8, -2) == 4   

def test_divide_by_zero():
    with pytest.raises(ValueError):
        division(5, 0)
