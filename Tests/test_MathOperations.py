import unittest

from MathOperations.addition import Addition
from MathOperations.division import Division
from MathOperations.multiplication import Multiplication
from MathOperations.subtraction import Subtraction

class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1,2))

    def test_calculator_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1,2))

    def test_MathOperations_multiplication(self):
        self.assertEqual(6, Multiplication.product(3,2))

    def test_MathOperations_division(self):
        self.assertEqual(3, Division.fraction(9,3))

if __name__ == '__main__':
    unittest.main()