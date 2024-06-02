from data.data_resampler import resample_data
from AlgorithmImports import *

class WeekAggregator:
    """
    Aggregates daily trade bars into weekly trade bars.

    Attributes:
        algorithm (QCAlgorithm): The trading algorithm instance.
        weekly_bars (dict): A dictionary to store aggregated weekly bars for each symbol.
    """

    def __init__(self, algorithm):
        """
        Initializes the WeekAggregator with the given algorithm.

        Args:
            algorithm (QCAlgorithm): The trading algorithm instance.
        """
        self.algorithm = algorithm
        self.weekly_bars = {}

    def update(self, data):
        """
        Updates the weekly bars with incoming daily trade bars.

        Args:
            data (Slice): The current data slice.

        Returns:
            None
        """
        for symbol, bars in data.Bars.items():
            if symbol not in self.weekly_bars:
                self.weekly_bars[symbol] = []

            resampled_df = resample_data(bars, 'W')

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
                self.weekly_bars[symbol].append(trade_bar)

    def get_weekly_bars(self, symbol):
        """
        Retrieves the aggregated weekly bars for a given symbol.

        Args:
            symbol (Symbol): The symbol for which to retrieve the weekly bars.

        Returns:
            list: A list of aggregated weekly trade bars.
        """
        return self.weekly_bars.get(symbol, [])
