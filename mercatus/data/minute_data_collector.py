
from AlgorithmImports import *

class MinuteDataCollector:
    """
    Collects minute-level data for a given symbol.

    Attributes:
        algorithm (QCAlgorithm): The trading algorithm instance.
        symbol (Symbol): The symbol for which to collect minute data.
        minute_data (list): A list to store the collected minute data.
    """

    def __init__(self, algorithm, symbol):
        """
        Initializes the MinuteDataCollector with the given algorithm and symbol.

        Args:
            algorithm (QCAlgorithm): The trading algorithm instance.
            symbol (Symbol): The symbol for which to collect minute data.
        """
        self.algorithm = algorithm
        self.symbol = symbol
        self.minute_data = []

    def collect_minute_data(self, data):
        """
        Collects minute data for the specified symbol.

        Args:
            data (Slice): The current data slice.

        Returns:
            None
        """
        if data.Bars.ContainsKey(self.symbol):
            self.minute_data.append(data[self.symbol])
