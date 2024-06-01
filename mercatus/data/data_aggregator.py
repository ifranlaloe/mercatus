import pandas as pd
from AlgorithmImports import *

class DataAggregator:
    def __init__(self, algorithm, symbol):
        self.algorithm = algorithm
        self.symbol = symbol
        self.minute_data = []

    def collect_minute_data(self, data):
        if data.Bars.ContainsKey(self.symbol):
            self.minute_data.append(data[self.symbol])

    def calculate_daily_bar_from_minute_data(self):
        if not self.minute_data:
            return []
        df = pd.DataFrame([[
            bar.Time, bar.Open, bar.High, bar.Low, bar.Close, bar.Volume
        ] for bar in self.minute_data], columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
        df.set_index('Time', inplace=True)
        daily_data = df.resample('D').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
        self.minute_data = []
        return [TradeBar(index, self.symbol, row['Open'], row['High'], row['Low'], row['Close'], row['Volume']) for index, row in daily_data.iterrows()]

    def resample_data(self, data, period):
        if not data:
            return []
        df = pd.DataFrame([[
            bar.Time, bar.Open, bar.High, bar.Low, bar.Close, bar.Volume
        ] for bar in data], columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
        df.set_index('Time', inplace=True)
        resampled_data = df.resample(period).agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
        return [TradeBar(index, self.symbol, row['Open'], row['High'], row['Low'], row['Close'], row['Volume']) for index, row in resampled_data.iterrows()]

    def convert_to_trade_bars(self, historical_data):
        return [TradeBar(bar.Time, self.symbol, bar.Open, bar.High, bar.Low, bar.Close, bar.Volume) for bar in historical_data]
