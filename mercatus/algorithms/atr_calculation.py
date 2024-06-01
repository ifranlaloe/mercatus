class ATRCalculator:
    """
    A class to calculate the Average True Range (ATR) from financial data.
    """
    
    def __init__(self, data):
        """
        Initialize the ATRCalculator with data.
        
        Parameters:
        data (list): A list of dictionaries containing 'high', 'low', and 'close' prices.
        """
        self.data = data

    def calculate(self):
        """
        Calculate the Average True Range (ATR).

        Returns:
        list: A list of ATR values.
        """
        atr_values = []
        for i in range(1, len(self.data)):
            high_low = self.data[i]['high'] - self.data[i]['low']
            high_close = abs(self.data[i]['high'] - self.data[i-1]['close'])
            low_close = abs(self.data[i]['low'] - self.data[i-1]['close'])
            tr = max(high_low, high_close, low_close)
            atr_values.append(tr)
        return atr_values
