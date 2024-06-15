# data/symbol.py

from data.minute_data_collector import MinuteDataCollector

class Symbol:
    def __init__(self, ticker):
        self.ticker = ticker
        self.minute_data_collector = MinuteDataCollector()
        # Initialize other aggregators as needed

    def collect_minute_data(self, data):
        self.minute_data_collector.collect_minute_data(data, self.ticker)
        # Call other aggregators as needed
