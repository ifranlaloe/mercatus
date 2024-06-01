from AlgorithmImports import *
from data.day_aggregator import DayAggregator
from data.week_aggregator import WeekAggregator
from data.month_aggregator import MonthAggregator

class AlgorithmInitializer:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def initialize(self):
        self.algorithm.SetStartDate(2023, 1, 1)
        self.algorithm.SetEndDate(2023, 12, 31)
        self.algorithm.SetCash(100000)
        
        # Set resolution based on mode
        resolution = Resolution.Minute
        if self.algorithm.LiveMode:
            resolution = Resolution.Tick
        
        self.algorithm.spy = self.algorithm.AddEquity("SPY", resolution).Symbol
        
        # Initialize aggregators
        self.algorithm.day_aggregator = DayAggregator(self.algorithm)
        self.algorithm.week_aggregator = WeekAggregator(self.algorithm)
        self.algorithm.month_aggregator = MonthAggregator(self.algorithm)

        self.algorithm.Schedule.On(self.algorithm.DateRules.EveryDay(self.algorithm.spy), self.algorithm.TimeRules.AfterMarketOpen(self.algorithm.spy, 1), self.algorithm.day_aggregator.update)
        self.algorithm.Schedule.On(self.algorithm.DateRules.WeekEnd(self.algorithm.spy), self.algorithm.TimeRules.AfterMarketOpen(self.algorithm.spy, 1), self.algorithm.week_aggregator.update)
        self.algorithm.Schedule.On(self.algorithm.DateRules.MonthEnd(self.algorithm.spy), self.algorithm.TimeRules.AfterMarketOpen(self.algorithm.spy, 1), self.algorithm.month_aggregator.update)
