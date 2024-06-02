from data.day_aggregator import DayAggregator
from data.week_aggregator import WeekAggregator
from data.month_aggregator import MonthAggregator
from data.minute_data_collector import MinuteDataCollector

class AggregatorInitializer:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def initialize_aggregators(self):
        self.algorithm.day_aggregator = DayAggregator(self.algorithm)
        self.algorithm.week_aggregator = WeekAggregator(self.algorithm)
        self.algorithm.month_aggregator = MonthAggregator(self.algorithm)
        self.algorithm.minute_data_collector = MinuteDataCollector(self.algorithm, self.algorithm.spy)

        self.algorithm.Schedule.On(self.algorithm.DateRules.EveryDay(self.algorithm.spy), 
                                   self.algorithm.TimeRules.AfterMarketOpen(self.algorithm.spy, 1), 
                                   self.algorithm.day_aggregator.update)
        self.algorithm.Schedule.On(self.algorithm.DateRules.WeekEnd(self.algorithm.spy), 
                                   self.algorithm.TimeRules.AfterMarketOpen(self.algorithm.spy, 1), 
                                   self.algorithm.week_aggregator.update)
        self.algorithm.Schedule.On(self.algorithm.DateRules.MonthEnd(self.algorithm.spy), 
                                   self.algorithm.TimeRules.AfterMarketOpen(self.algorithm.spy, 1), 
                                   self.algorithm.month_aggregator.update)
