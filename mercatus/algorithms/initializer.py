from AlgorithmImports import *
from data.data_aggregator import DataAggregator

class AlgorithmInitializer:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def initialize(self):
        self.algorithm.SetStartDate(2023, 1, 1)
        self.algorithm.SetEndDate(2023, 12, 31)
        self.algorithm.SetCash(100000)
        
        self.algorithm.spy = self.algorithm.AddEquity("SPY", Resolution.Minute if self.algorithm.LiveMode else Resolution.Daily).Symbol
        self.algorithm.data_aggregator = DataAggregator(self.algorithm.spy, self.algorithm.LiveMode)

        self.algorithm.Schedule.On(self.algorithm.DateRules.EveryDay(self.algorithm.spy), self.algorithm.TimeRules.AfterMarketOpen(self.algorithm.spy, 1), self.algorithm.UpdateDailyData)
        self.algorithm.Schedule.On(self.algorithm.DateRules.WeekEnd(self.algorithm.spy), self.algorithm.TimeRules.AfterMarketOpen(self.algorithm.spy, 1), self.algorithm.UpdateWeeklyData)
        self.algorithm.Schedule.On(self.algorithm.DateRules.MonthEnd(self.algorithm.spy), self.algorithm.TimeRules.AfterMarketOpen(self.algorithm.spy, 1), self.algorithm.UpdateMonthlyData)
