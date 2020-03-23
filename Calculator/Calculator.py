from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.division import Division
from MathOperations.multiplication import Multiplication
from MathOperations.root import Root



class Calculator:
    Result = 0

    def __init__(self):
        pass

    def sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def fraction(self, a, b):
        self.Result = Division.fraction(a, b)
        return self.Result

    def product(self, a, b):
        self.Result = Multiplication.product(a, b)

    def nthroot(self, a, b):
        self.Result = Root.root(a, b)
        return self.Result
