class DataHandler:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def on_data(self, data):
        self.algorithm.data_aggregator.collect_minute_data(data)
        if not self.algorithm.Portfolio.Invested:
            self.algorithm.SetHoldings("SPY", 1)
            self.algorithm.Debug("Purchased Stock")
