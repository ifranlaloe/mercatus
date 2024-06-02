from data.data_resampler import resample_data
from AlgorithmImports import *

class DayAggregator:
    """
    Aggregates incoming tick or minute data into daily trade bars.

    Attributes:
        algorithm (QCAlgorithm): The trading algorithm instance.
        daily_bars (dict): A dictionary to store aggregated daily bars for each symbol.
    """

    def __init__(self, algorithm):
        """
        Initializes the DayAggregator with the given algorithm.

        Args:
            algorithm (QCAlgorithm): The trading algorithm instance.
        """
        self.algorithm = algorithm
        self.daily_bars = {}

    def update(self, data):
        """
        Updates the daily bars with incoming data.

        Args:
            data (Slice): The current data slice.

        Returns:
            None
        """
        for symbol, bars in data.Bars.items():
            if symbol not in self.daily_bars:
                self.daily_bars[symbol] = []

            resampled_df = resample_data(bars, 'D')

            for idx, row in resampled_df.iterrows():
                trade_bar = TradeBar(
                    Time=idx,
                    Open=row['open'],
                    High=row['high'],
                    Low=row['low'],
                    Close=row['close'],
                    Volume=row['volume'],
                    Symbol=symbol
                )
                self.daily_bars[symbol].append(trade_bar)

    def get_daily_bars(self, symbol):
        """
        Retrieves the aggregated daily bars for a given symbol.

        Args:
            symbol (Symbol): The symbol for which to retrieve the daily bars.

        Returns:
            list: A list of aggregated daily trade bars.
        """
        return self.daily_bars.get(symbol, [])
