from AlgorithmImports import *
from data.data_resampler import DataResampler

class MonthAggregator:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.symbol = algorithm.spy  # Assuming spy is the symbol of interest
        self.monthly_data = []
        self.data_resampler = DataResampler(self.symbol)

    def update(self):
        self.monthly_data = self.data_resampler.resample_data(self.algorithm.day_aggregator.daily_data, 'M')
