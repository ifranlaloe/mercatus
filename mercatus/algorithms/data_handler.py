
class DataHandler:
    """
    Handles the data for the trading algorithm.

    Attributes:
        algorithm (QCAlgorithm): The trading algorithm instance.
    """

    def __init__(self, algorithm):
        """
        Initializes the DataHandler with the given algorithm.

        Args:
            algorithm (QCAlgorithm): The trading algorithm instance.
        """
        self.algorithm = algorithm

    def on_data(self, data):
        """
        Processes the incoming data.

        Args:
            data (Slice): The current data slice.

        Returns:
            None
        """
        if not data.Bars.ContainsKey(self.algorithm.spy):
            self.algorithm.Debug("No data for SPY")
            return

        self.algorithm.minute_data_collector.collect_minute_data(data)
        
        if not self.algorithm.Portfolio.Invested:
            self.algorithm.SetHoldings("SPY", 1)
            self.algorithm.Debug("Purchased Stock")
        else:
            self.algorithm.Debug("Already invested")
