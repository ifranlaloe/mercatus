from algorithms.symbol import Symbol


class EquityInitializer:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.symbols = {
            "SPY": Symbol("SPY"),
            # Add other symbols as needed
        }

    def add_equity(self, symbol, resolution):
        return self.algorithm.AddEquity(symbol, resolution).Symbol
