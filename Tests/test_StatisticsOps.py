import unittest
from Statistics.Statistics import Statistics

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.statistics = Statistics()

    def test_statistics_calculator_return_variance(self):
        data = [1, 2, 3, 4, 5, 6]
        result = self.statistics.variance(data)
        self.assertEqual(2.9166666666666665, result)
