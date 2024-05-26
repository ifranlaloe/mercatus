import pandas as pd
from AlgorithmImports import *

class LeanTradingStrategy(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2023, 1, 1)
        self.SetEndDate(2023, 12, 31)
        self.SetCash(100000)
        
        # Add SPY data
        self.spy = self.AddEquity("SPY", Resolution.Minute if self.LiveMode else Resolution.Daily).Symbol
        
        # Initialize lists to store historical data
        self.minute_data = []
        self.daily_data = []
        self.weekly_data = []
        self.monthly_data = []

        # Schedule the daily, weekly, and monthly aggregation
        self.Schedule.On(self.DateRules.EveryDay(self.spy), self.TimeRules.AfterMarketOpen(self.spy, 1), self.UpdateDailyData)
        self.Schedule.On(self.DateRules.WeekEnd(self.spy), self.TimeRules.AfterMarketOpen(self.spy, 1), self.UpdateWeeklyData)
        self.Schedule.On(self.DateRules.MonthEnd(self.spy), self.TimeRules.AfterMarketOpen(self.spy, 1), self.UpdateMonthlyData)

    def OnData(self, data):
        """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
        Arguments:
            data: Slice object keyed by symbol containing the stock data
        """
        if self.LiveMode and data.Bars.ContainsKey(self.spy):
            minute_bar = data[self.spy]
            self.minute_data.append(minute_bar)
        
        # Original functionality
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)
            self.Debug("Purchased Stock")

    def UpdateDailyData(self):
        if self.LiveMode:
            self.CalculateDailyBarFromMinuteData()
        else:
            self.daily_data = self.History(self.spy, 1, Resolution.Daily)
            self.ConvertToTradeBars(self.daily_data)
        
    def CalculateDailyBarFromMinuteData(self):
        if len(self.minute_data) == 0:
            return
        
        # Resample minute data to daily
        df = pd.DataFrame([[
            bar.Time, bar.Open, bar.High, bar.Low, bar.Close, bar.Volume
        ] for bar in self.minute_data], columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
        
        df.set_index('Time', inplace=True)
        daily_data = df.resample('D').agg({
            'Open': 'first',
            'High': 'max',
            'Low': 'min',
            'Close': 'last',
            'Volume': 'sum'
        })
        
        # Convert daily data back to TradeBar objects
        self.daily_data = [TradeBar(
            index, 
            self.spy, 
            row['Open'], 
            row['High'], 
            row['Low'], 
            row['Close'], 
            row['Volume']) for index, row in daily_data.iterrows()]
        
        # Clear minute data after processing
        self.minute_data = []

    def UpdateWeeklyData(self):
        self.ResampleData('W-FRI', self.weekly_data)

    def UpdateMonthlyData(self):
        self.ResampleData('M', self.monthly_data)

    def ResampleData(self, period, target_list):
        if len(self.daily_data) == 0:
            return
        
        # Resample daily data to the desired period
        df = pd.DataFrame([[
            bar.Time, bar.Open, bar.High, bar.Low, bar.Close, bar.Volume
        ] for bar in self.daily_data], columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
        
        df.set_index('Time', inplace=True)
        resampled_data = df.resample(period).agg({
            'Open': 'first',
            'High': 'max',
            'Low': 'min',
            'Close': 'last',
            'Volume': 'sum'
        })
        
        # Convert resampled data back to TradeBar objects
        target_list.clear()
        target_list.extend([TradeBar(
            index, 
            self.spy, 
            row['Open'], 
            row['High'], 
            row['Low'], 
            row['Close'], 
            row['Volume']) for index, row in resampled_data.iterrows()])

    def ConvertToTradeBars(self, historical_data):
        self.daily_data = [TradeBar(
            bar.Time,
            self.spy,
            bar.Open,
            bar.High,
            bar.Low,
            bar.Close,
            bar.Volume
        ) for bar in historical_data]

    def OnEndOfDay(self):
        # Optionally log or process end-of-day data
        pass
