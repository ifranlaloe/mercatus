# algorithms/initializers/watcher_initializer.py

from data.symbol import Symbol

class WatcherInitializer:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.watchers = set()

    def initialize(self):
        # Call UpdateWatchers once at startup
        self.UpdateWatchers()
        
        # Schedule the universe update at the start of each trading day
        self.algorithm.Schedule.On(
            self.algorithm.DateRules.EveryDay("SPY"),
            self.algorithm.TimeRules.AfterMarketOpen("SPY", 1),
            self.UpdateWatchers
        )

    def UpdateWatchers(self):
        # Fetch assets to watch
        assets = self.GetAssetsToWatch()
        
        # Convert to Symbol objects and set for easy comparison
        new_watchers = {Symbol(ticker) for ticker in assets}
        
        # Determine symbols to add and remove
        symbols_to_add = new_watchers - self.watchers
        symbols_to_remove = self.watchers - new_watchers

        # Add new symbols
        self.AddSecurities(symbols_to_add)

        # Remove old symbols if no open positions
        self.RemoveSecurities(symbols_to_remove)

        # Update current watchers, keeping those with open positions
        self.watchers = (self.watchers - symbols_to_remove) | symbols_to_add

    def AddSecurities(self, symbols):
        for symbol in symbols:
            symbol.add_to_algorithm(self.algorithm)

    def RemoveSecurities(self, symbols):
        for symbol in symbols:
            if not self.algorithm.Portfolio[symbol.ticker].Invested:
                self.algorithm.RemoveSecurity(symbol.ticker)
            else:
                # Keep the symbol in watchers if it has an open position
                self.watchers.add(symbol)

    def GetAssetsToWatch(self):
        # Mock function to return a list of assets to watch
        # In practice, you would fetch this from a data source
        return ["AAPL", "MSFT", "GOOGL", "AMZN", "FB", "TSLA"]
