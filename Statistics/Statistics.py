from Calculator.Calculator import Calculator
from StatisticsOps.mean import Mean
from StatisticsOps.mode import Mode

from Random.random_Op import Random_num;

class Statistics(Calculator):

    def mean(self, data):
        self.Result = Mean(data)
        return self.Result

    def mode(self, data):
        self.Result = Mode.mode(data)
        return self.Result