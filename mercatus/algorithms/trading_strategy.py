from AlgorithmImports import *
from data.data_aggregator import DataAggregator

class TradingStrategy(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2023, 1, 1)
        self.SetEndDate(2023, 12, 31)
        self.SetCash(100000)
        
        self.spy = self.AddEquity("SPY", Resolution.Minute if self.LiveMode else Resolution.Daily).Symbol
        self.data_aggregator = DataAggregator(self.spy, self.LiveMode)

        self.Schedule.On(self.DateRules.EveryDay(self.spy), self.TimeRules.AfterMarketOpen(self.spy, 1), self.UpdateDailyData)
        self.Schedule.On(self.DateRules.WeekEnd(self.spy), self.TimeRules.AfterMarketOpen(self.spy, 1), self.UpdateWeeklyData)
        self.Schedule.On(self.DateRules.MonthEnd(self.spy), self.TimeRules.AfterMarketOpen(self.spy, 1), self.UpdateMonthlyData)

    def OnData(self, data):
        self.data_aggregator.collect_minute_data(data)
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)
            self.Debug("Purchased Stock")

    def UpdateDailyData(self):
        self.data_aggregator.update_daily_data()

    def UpdateWeeklyData(self):
        self.data_aggregator.update_weekly_data()

    def UpdateMonthlyData(self):
        self.data_aggregator.update_monthly_data()
