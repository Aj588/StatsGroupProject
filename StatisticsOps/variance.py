from numpy import absolute, asarray
from StatisticsOps import mean

class Variance:
    @staticmethod
    def variance(data):
        return mean.Mean(absolute(asarray(data) - mean.Mean(data))**2)


