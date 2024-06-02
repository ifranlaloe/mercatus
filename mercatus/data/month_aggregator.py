from data.data_resampler import resample_data
from AlgorithmImports import *

class MonthAggregator:
    """
    Aggregates daily trade bars into monthly trade bars.

    Attributes:
        algorithm (QCAlgorithm): The trading algorithm instance.
        monthly_bars (dict): A dictionary to store aggregated monthly bars for each symbol.
    """

    def __init__(self, algorithm):
        """
        Initializes the MonthAggregator with the given algorithm.

        Args:
            algorithm (QCAlgorithm): The trading algorithm instance.
        """
        self.algorithm = algorithm
        self.monthly_bars = {}

    def update(self, data):
        """
        Updates the monthly bars with incoming daily trade bars.

        Args:
            data (Slice): The current data slice.

        Returns:
            None
        """
        for symbol, bars in data.Bars.items():
            if symbol not in self.monthly_bars:
                self.monthly_bars[symbol] = []

            resampled_df = resample_data(bars, 'M')

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
                self.monthly_bars[symbol].append(trade_bar)

    def get_monthly_bars(self, symbol):
        """
        Retrieves the aggregated monthly bars for a given symbol.

        Args:
            symbol (Symbol): The symbol for which to retrieve the monthly bars.

        Returns:
            list: A list of aggregated monthly trade bars.
        """
        return self.monthly_bars.get(symbol, [])
