from StatisticsOps import variance
from StatisticsOps import StandardDeviation


def test_StatisticsOps_variance(self):
    self.assertEqual(844.0474999999999, variance.variance(self.testData))


def test_StatisticOps_StandardDeviation(self):
    self.assertEqual(1.0008215555060946, StandardDeviation.StandardDeviation(self.testData))
