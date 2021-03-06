import unittest
from random import random

import unittest
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    # Test Mean
    def test_statistics_calculator_return_mean(self):
        data = [1, 2, 3, 4, 5]
        result = self.statistics.mean(data)
        self.assertEqual(3, result)

    # Test Mode
    def test_statistics_calculator_return_mode(self):
        data = [1, 2, 3, 3, 4, 5]
        result = self.statistics.mode(data)
        self.assertEqual(3, result)

    def test_statistics_calculator_return_NoMode(self):
        data = [1, 2, 3, 4, 5]
        result = self.statistics.mode(data)
        self.assertEqual('no mode', result)

    # Test Median
    def test_statistics_calculator_return_median(self):
        data = [2, 4, 6, 8, 10]
        result = self.statistics.median(data)
        self.assertEqual(6, result)


if __name__ == '__main__':
    unittest.main()
