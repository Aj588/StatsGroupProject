from StatisticsOps.quartiles import Quartiles
from StatisticsOps.variance import Variance


def test_StatisticsOps_variance(self):
    self.assertEqual(844.0474999999999, Variance.variance(self.testData))


def test_StatisticOps_quartiles(self):
    self.assertEqual([12.75, 27.5, 72.25], Quartiles.quartiles(self.testData))
