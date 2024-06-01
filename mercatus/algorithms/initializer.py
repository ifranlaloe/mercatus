from algorithms.initializers.algorithm_settings import AlgorithmSettings
from algorithms.initializers.resolution_settings import ResolutionSettings
from algorithms.initializers.equity_initializer import EquityInitializer
from algorithms.initializers.aggregator_initializer import AggregatorInitializer

class AlgorithmInitializer:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def initialize(self):
        # Set dates and cash
        settings = AlgorithmSettings(self.algorithm)
        settings.set_dates_and_cash((2023, 1, 1), (2023, 12, 31), 100000)
        
        # Set resolution
        resolution_settings = ResolutionSettings(self.algorithm)
        resolution = resolution_settings.set_resolution()

        # Add equity
        equity_initializer = EquityInitializer(self.algorithm)
        self.algorithm.spy = equity_initializer.add_equity("SPY", resolution)

        # Initialize and schedule aggregators
        aggregator_initializer = AggregatorInitializer(self.algorithm)
        aggregator_initializer.initialize_aggregators()
