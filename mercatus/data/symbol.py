# data/symbol.py

from data.minute_data_collector import MinuteDataCollector
from AlgorithmImports import Resolution

class Symbol:
    def __init__(self, ticker, algorithm):
        self.ticker = ticker
        self.algorithm = algorithm
        self.minute_data_collector = MinuteDataCollector()
        # Initialize other aggregators as needed

    def collect_minute_data(self, data):
        self.minute_data_collector.collect_minute_data(data, self.ticker)
        # Call other aggregators as needed

    def add_to_algorithm(self):
        # Set the resolution here based on live mode
        resolution = Resolution.Tick if self.algorithm.LiveMode else Resolution.Minute
        self.algorithm.AddEquity(self.ticker, resolution)
