from AlgorithmImports import *
from algorithms.initializer import AlgorithmInitializer
from algorithms.data_handler import DataHandler

class TradingStrategy(QCAlgorithm):
    def Initialize(self):
        self.initializer = AlgorithmInitializer(self)
        self.initializer.initialize()
        self.data_handler = DataHandler(self)
        # Other initialization code

    def OnData(self, data):
        self.data_handler.on_data(data)
