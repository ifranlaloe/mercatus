from data.minute_data_collector import MinuteDataCollector

class Symbol:
    def __init__(self, symbol_name):
        self.symbol_name = symbol_name
        self.minute_data_collector = MinuteDataCollector()
        # Initialize other aggregators as needed

    def collect_minute_data(self, data):
        self.minute_data_collector.collect_minute_data(data, self.symbol_name)
        # Call other aggregators as needed
