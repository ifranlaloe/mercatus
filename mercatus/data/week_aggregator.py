
"""
Module for aggregating weekly data.

This module provides functionalities for aggregating data on a weekly basis.
"""

from AlgorithmImports import *
from data.data_resampler import DataResampler

class WeekAggregator:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.symbol = algorithm.spy  # Assuming spy is the symbol of interest
        self.weekly_data = []
        self.data_resampler = DataResampler(self.symbol)

    def update(self):
        self.weekly_data = self.data_resampler.resample_data(self.algorithm.day_aggregator.daily_data, 'W-FRI')

