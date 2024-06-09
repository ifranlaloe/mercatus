# algorithms/data_handler.py

class DataHandler:
    def __init__(self, algorithm, watcher_initializer):
        self.algorithm = algorithm
        self.watcher_initializer = watcher_initializer

    def OnData(self, data):
        # Trading logic based on the current symbols in watchers
        for symbol in self.watcher_initializer.watchers:
            if symbol.ticker in data:
                # Collect minute data for each symbol
                symbol.collect_minute_data(data[symbol.ticker])

                # Your trading logic here, for example:
                self.algorithm.Debug(f"Processing data for {symbol.ticker}")
