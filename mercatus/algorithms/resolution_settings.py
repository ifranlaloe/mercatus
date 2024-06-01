from AlgorithmImports import *

class ResolutionSettings:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def set_resolution(self):
        return Resolution.Tick if self.algorithm.LiveMode else Resolution.Minute
