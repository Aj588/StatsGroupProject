from Calculator.Calculator import Calculator
from StatisticsOps.mean import Mean
from StatisticsOps.mode import Mode
from StatisticsOps.median import Median
from StatisticsOps.variance import Variance
from StatisticsOps.quartile import Quartile

#from Random.random_Op import Random_num;


class Statistics(Calculator):

    def mean(self, data):
        self.Result = Mean(data)
        return self.Result

    def mode(self, data):
        self.Result = Mode.mode(data)
        return self.Result

    def median(self, data):
        self.Result = Median.median(data)
        return self.Result

    def variance(self, data):
        self.Result = Variance.variance(data)
        return self.Result

    def quartile(self, data, q, axis, kdims):
        self.Result = Quartile.quartile(data, q, axis, kdims)
        return self.Result



