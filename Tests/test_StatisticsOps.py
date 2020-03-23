from StatisticsOps import variance
from StatisticsOps import quartiles


def test_StatisticsOps_variance(self):
    self.assertEqual(844.0474999999999, variance.variance(self.testData))

def test_StatisticOps_quartiles(self):
    self.assertEqual([12.75, 27.5, 72.25], quartiles.quartiles(self.testData))
