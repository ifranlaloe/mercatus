import pandas as pd

def resample_data(bars, freq):
    """
    Resamples the given trade bars to the specified frequency.

    Args:
        bars (list of TradeBar): The trade bars to resample.
        freq (str): The frequency string for resampling (e.g., 'D' for daily, 'W' for weekly).

    Returns:
        pd.DataFrame: A DataFrame with the resampled trade bars.
    """
    df = pd.DataFrame({
        'time': [bar.Time for bar in bars],
        'open': [bar.Open for bar in bars],
        'high': [bar.High for bar in bars],
        'low': [bar.Low for bar in bars],
        'close': [bar.Close for bar in bars],
        'volume': [bar.Volume for bar in bars]
    })

    df.set_index('time', inplace=True)
    
    resampled_df = df.resample(freq).agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum'
    }).dropna()
    
    return resampled_df
