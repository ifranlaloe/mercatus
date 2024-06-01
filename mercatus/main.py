from AlgorithmImports import *
from algorithms.initializer import AlgorithmInitializer
from algorithms.data_handler import DataHandler

class TradingStrategy(QCAlgorithm):
    """
    The main entrypoint of the Lean project. After trial and error it was determined that the QCAlgorithm
    is required to be a part of the main.py
    """    

    def Initialize(self):
        self.initializer = AlgorithmInitializer(self)
        self.initializer.initialize()
        self.data_handler = DataHandler(self)

    def OnData(self, data):
        self.data_handler.on_data(data)
