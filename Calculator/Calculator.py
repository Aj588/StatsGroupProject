from MathOperations.addition import Addition

class Calculator:
    Result = 0

    def __init__(self):
        pass

    def sum(self, a, b):
        self.Result = Addition.sum(a, b)
        returm self.Result