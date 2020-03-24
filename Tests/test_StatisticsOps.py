import unittest
from Statistics.Statistics import Statistics

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_statistics_calculator_return_variance(self):
        data = [1, 2, 3, 4, 5, 6]
        result = self.statistics.variance(data)
        self.assertEqual(2.9166666666666665, result)

    def test_statistics_calculator_return_quartiles(self):
        data = [2, 6, 7]
        result = self.statistics.quartile(data, 0.25, 0, None)
        self.assertEqual(4, result)

if __name__ == '__main__':
    unittest.main()