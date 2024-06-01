from data.data_aggregator import DataAggregator

class WeekAggregator:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.data_aggregator = DataAggregator(self.algorithm, self.algorithm.spy, self.algorithm.LiveMode)

    def update(self):
        self.data_aggregator.update_weekly_data()
