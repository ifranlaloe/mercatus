from AlgorithmImports import *

class MinuteDataCollector:
    def __init__(self, algorithm, symbol):
        self.algorithm = algorithm
        self.symbol = symbol
        self.minute_data = []

    def collect_minute_data(self, data):
        if data.Bars.ContainsKey(self.symbol):
            self.minute_data.append(data[self.symbol])
