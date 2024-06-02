import unittest
from unittest.mock import MagicMock

# Assuming the MinuteDataCollector class is defined as provided
class MinuteDataCollector:
    def __init__(self, algorithm, symbol):
        self.algorithm = algorithm
        self.symbol = symbol
        self.minute_data = []

    def collect_minute_data(self, data):
        if data.Bars.ContainsKey(self.symbol):
            self.minute_data.append(data[self.symbol])

# Define a test case for MinuteDataCollector
class TestMinuteDataCollector(unittest.TestCase):

    def setUp(self):
        # Setup a mock algorithm and symbol
        self.algorithm = MagicMock()
        self.symbol = "AAPL"
        self.collector = MinuteDataCollector(self.algorithm, self.symbol)

    def test_collect_minute_data_with_valid_data(self):
        # Create a mock data object with the symbol
        data = MagicMock()
        data.Bars.ContainsKey.return_value = True
        data.__getitem__.return_value = "sample_data"

        # Call collect_minute_data
        self.collector.collect_minute_data(data)

        # Check if the minute_data list is updated correctly
        self.assertEqual(self.collector.minute_data, ["sample_data"])

    def test_collect_minute_data_with_invalid_data(self):
        # Create a mock data object without the symbol
        data = MagicMock()
        data.Bars.ContainsKey.return_value = False

        # Call collect_minute_data
        self.collector.collect_minute_data(data)

        # Check if the minute_data list remains empty
        self.assertEqual(self.collector.minute_data, [])

# Run the tests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMinuteDataCollector))
