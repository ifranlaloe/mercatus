from AlgorithmImports import *
from algorithms.initializer import AlgorithmInitializer
from algorithms.data_handler import DataHandler
from data.data_aggregator import DataAggregator

class TradingStrategy(QCAlgorithm):

    def Initialize(self):
        self.initializer = AlgorithmInitializer(self)
        self.initializer.initialize()

    def OnData(self, data):
        self.data_handler = DataHandler(self)
        self.data_handler.on_data(data)

    def UpdateDailyData(self):
        self.data_aggregator.update_daily_data()

    def UpdateWeeklyData(self):
        self.data_aggregator.update_weekly_data()

    def UpdateMonthlyData(self):
        self.data_aggregator.update_monthly_data()
