class DataHandler:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def on_data(self, data):
        if not data.Bars.ContainsKey(self.algorithm.spy):
            self.algorithm.Debug("No data for SPY")
            return

        self.algorithm.minute_data_collector.collect_minute_data(data)
        
        if not self.algorithm.Portfolio.Invested:
            self.algorithm.SetHoldings("SPY", 1)
            self.algorithm.Debug("Purchased Stock")
        else:
            self.algorithm.Debug("Already invested")
