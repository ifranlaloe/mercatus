
"""
Module for aggregating daily data.

This module provides functionalities for aggregating data on a daily basis.
"""

from AlgorithmImports import *
from data.minute_data_collector import MinuteDataCollector
from data.data_resampler import DataResampler

class DayAggregator:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.symbol = algorithm.spy  # Assuming spy is the symbol of interest
        self.live_mode = algorithm.LiveMode
        self.daily_data = []
        self.minute_data_collector = MinuteDataCollector(algorithm, self.symbol)
        self.data_resampler = DataResampler(self.symbol)

    def update(self):
        if self.live_mode:
            self.daily_data = self.data_resampler.calculate_daily_bar_from_minute_data(self.minute_data_collector.minute_data)
        else:
            historical_data = self.algorithm.History(self.symbol, 1, Resolution.Daily)
            self.daily_data = self.data_resampler.convert_to_trade_bars(historical_data)

