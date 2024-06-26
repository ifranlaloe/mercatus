
from data.day_aggregator import DayAggregator
from data.week_aggregator import WeekAggregator
from data.month_aggregator import MonthAggregator
from data.minute_data_collector import MinuteDataCollector

class AggregatorInitializer:
    """
    Initializes the data aggregators for the trading algorithm.

    Attributes:
        algorithm (QCAlgorithm): The trading algorithm instance.
    """

    def __init__(self, algorithm):
        """
        Initializes the AggregatorInitializer with the given algorithm.

        Args:
            algorithm (QCAlgorithm): The trading algorithm instance.
        """
        self.algorithm = algorithm

    def initialize_aggregators(self):
        """
        Initializes and schedules the data aggregators.

        Returns:
            None
        """
        self.algorithm.day_aggregator = DayAggregator(self.algorithm)
        self.algorithm.week_aggregator = WeekAggregator(self.algorithm)
        self.algorithm.month_aggregator = MonthAggregator(self.algorithm)

        self.algorithm.Schedule.On(self.algorithm.DateRules.EveryDay(self.algorithm.spy), 
                                   self.algorithm.TimeRules.AfterMarketOpen(self.algorithm.spy, 1), 
                                   self.algorithm.day_aggregator.update)
        self.algorithm.Schedule.On(self.algorithm.DateRules.WeekEnd(self.algorithm.spy), 
                                   self.algorithm.TimeRules.AfterMarketOpen(self.algorithm.spy, 1), 
                                   self.algorithm.week_aggregator.update)
        self.algorithm.Schedule.On(self.algorithm.DateRules.MonthEnd(self.algorithm.spy), 
                                   self.algorithm.TimeRules.AfterMarketOpen(self.algorithm.spy, 1), 
                                   self.algorithm.month_aggregator.update)
