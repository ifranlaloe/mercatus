# algorithms/initializers/algorithm_initializer.py

from algorithms.initializers.algorithm_settings import AlgorithmSettings
from algorithms.initializers.watcher_initializer import WatcherInitializer
from algorithms.initializers.aggregator_initializer import AggregatorInitializer
from algorithms.data_handler import DataHandler

class AlgorithmInitializer:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.data_handler = None

    def initialize(self):
        # Set dates and cash
        settings = AlgorithmSettings(self.algorithm)
        settings.set_dates_and_cash((2023, 1, 1), (2023, 12, 31), 100000)

        # Initialize and schedule watchers
        watcher_initializer = WatcherInitializer(self.algorithm)
        watcher_initializer.initialize()

        # Initialize and schedule aggregators
        aggregator_initializer = AggregatorInitializer(self.algorithm)
        aggregator_initializer.initialize_aggregators()

        # Initialize DataHandler
        self.data_handler = DataHandler(self.algorithm, watcher_initializer)
