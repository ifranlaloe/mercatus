from AlgorithmImports import *
from algorithms.algorithm_initializer import AlgorithmInitializer
from algorithms.data_handler import DataHandler

# main.py
class Main(QCAlgorithm):
    def Initialize(self):
        # Initialize the algorithm using AlgorithmInitializer
        initializer = AlgorithmInitializer(self)
        initializer.initialize()

        # Set the data handler from the initializer
        self.data_handler = initializer.data_handler

    def OnData(self, data):
        # Delegate OnData handling to the DataHandler
        self.data_handler.OnData(data)