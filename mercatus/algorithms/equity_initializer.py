class EquityInitializer:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def add_equity(self, symbol, resolution):
        return self.algorithm.AddEquity(symbol, resolution).Symbol
