import pandas as pd
from AlgorithmImports import *

class DataAggregator:
    def __init__(self, symbol, live_mode):
        self.symbol = symbol
        self.live_mode = live_mode
        self.minute_data = []
        self.daily_data = []
        self.weekly_data = []
        self.monthly_data = []

    def collect_minute_data(self, data):
        if self.live_mode and data.Bars.ContainsKey(self.symbol):
            self.minute_data.append(data[self.symbol])

    def update_daily_data(self):
        if self.live_mode:
            self.calculate_daily_bar_from_minute_data()
        else:
            self.daily_data = self.history(self.symbol, 1, Resolution.Daily)
            self.convert_to_trade_bars(self.daily_data)

    def calculate_daily_bar_from_minute_data(self):
        if not self.minute_data:
            return
        df = pd.DataFrame([[
            bar.Time, bar.Open, bar.High, bar.Low, bar.Close, bar.Volume
        ] for bar in self.minute_data], columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
        df.set_index('Time', inplace=True)
        daily_data = df.resample('D').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
        self.daily_data = [TradeBar(index, self.symbol, row['Open'], row['High'], row['Low'], row['Close'], row['Volume']) for index, row in daily_data.iterrows()]
        self.minute_data = []

    def update_weekly_data(self):
        self.resample_data('W-FRI', self.weekly_data)

    def update_monthly_data(self):
        self.resample_data('M', self.monthly_data)

    def resample_data(self, period, target_list):
        if not self.daily_data:
            return
        df = pd.DataFrame([[
            bar.Time, bar.Open, bar.High, bar.Low, bar.Close, bar.Volume
        ] for bar in self.daily_data], columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
        df.set_index('Time', inplace=True)
        resampled_data = df.resample(period).agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
        target_list.clear()
        target_list.extend([TradeBar(index, self.symbol, row['Open'], row['High'], row['Low'], row['Close'], row['Volume']) for index, row in resampled_data.iterrows()])

    def convert_to_trade_bars(self, historical_data):
        self.daily_data = [TradeBar(bar.Time, self.symbol, bar.Open, bar.High, bar.Low, bar.Close, bar.Volume) for bar in historical_data]
