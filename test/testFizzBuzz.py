from unittest import TestCase
from src.fizzbuzz import FizzBuzz

import io
import sys


class TestFizzBuzz(TestCase):
    """test class of fizzbuzz.py
    """

    def test_convert_when_1_return_1(self):
        """test convert with 1 for FizzBuzz
        """
        number  = 1
        expected = 1
        fb = FizzBuzz()
        actual = fb.convert(number)
        self.assertEqual(expected, actual)

    def test_convert_when_3_return_Fizz(self):
        """test convert with 3 for FizzBuzz
        """
        number  = 3
        expected = "Fizz"
        fb = FizzBuzz()
        actual = fb.convert(number)
        self.assertEqual(expected, actual)
        
    def test_say(self):
        """test method for FizzBuzz
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        number  = 1
        expected = "1\n"
        fb = FizzBuzz()
        fb.say(number)
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, capturedOutput.getvalue())
        
if __name__ == "__main__":
    unittest.main()
