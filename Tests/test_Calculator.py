import unittest
from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_calculator_return_sum(self):
        calculator = Calculator()
        result = calculator.sum(1, 2)
        self.assertEqual(result, 3)

    def test_calculator_return_difference(self):
        calculator = Calculator()
        result = calculator.difference(1, 2)
        self.assertEqual(result, -1)

    def test_calculator_return_fraction(self):
        calculator = Calculator()
        result = calculator.fraction(10, 5)
        self.assertEqual(result, 2)

    def test_calculator_access_sum_result(self):
        calculator = Calculator()
        calculator.sum(1, 2)
        self.assertEqual(calculator.Result, 3)

    def test_calculator_access_difference_result(self):
        calculator = Calculator()
        calculator.difference(1, 2)
        self.assertEqual(calculator.Result, -1)

    def test_calculator_access_fraction_result(self):
        calculator = Calculator()
        calculator.fraction(10, 5)
        self.assertEqual(calculator.Result, 2)

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        calculator3 = Calculator()
        calculator3.sum(calculator1.sum(1, 2), calculator2.difference(3, 4))
        self.assertEqual(2, calculator3.Result)

if __name__ == '__main__':
    unittest.main()
