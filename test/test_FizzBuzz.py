from src.fizzbuzz import FizzBuzz

import sys

def test_convert_when_1_return_1():
    number  = 1
    expected = 1
    fb = FizzBuzz()
    actual = fb.convert(number)
    assert expected == actual

def test_convert_when_3_return_Fizz():
    """test convert with 3 for FizzBuzz
    """
    number  = 3
    expected = "Fizz"
    fb = FizzBuzz()
    actual = fb.convert(number)
    assert expected == actual
    
        
def test_stdout(capfd):
    """test method for FizzBuzz
    """
    number  = 1
    expected = "1\n"
    fb = FizzBuzz()
    fb.say(number)
    actual, dmy = capfd.readouterr()
    assert expected, actual
