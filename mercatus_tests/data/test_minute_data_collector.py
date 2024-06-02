import unittest
from mercatus.algorithms.symbol import Symbol

class TestMinuteDataCollector(unittest.TestCase):

    def setUp(self):
        self.symbol = Symbol("AAPL")

    def test_collect_minute_data_with_valid_data(self):
        data = {"AAPL": "sample_data"}
        self.symbol.collect_minute_data(data)
        self.assertEqual(self.symbol.minute_data_collector.minute_data, ["sample_data"])

    def test_collect_minute_data_with_invalid_data(self):
        data = {"GOOG": "sample_data"}
        self.symbol.collect_minute_data(data)
        self.assertEqual(self.symbol.minute_data_collector.minute_data, [])

if __name__ == '__main__':
    unittest.main()
