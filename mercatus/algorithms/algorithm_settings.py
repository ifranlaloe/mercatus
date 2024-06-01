class AlgorithmSettings:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def set_dates_and_cash(self, start_date, end_date, cash):
        self.algorithm.SetStartDate(*start_date)
        self.algorithm.SetEndDate(*end_date)
        self.algorithm.SetCash(cash)
