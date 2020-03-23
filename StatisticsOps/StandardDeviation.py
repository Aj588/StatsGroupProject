from MathOperations.root import Root
from StatisticsOps.variance import Variance


class StandardDeviation:
    @staticmethod
    def standardDeviation(data):
        return Root.root(Variance.variance(data), 2)
