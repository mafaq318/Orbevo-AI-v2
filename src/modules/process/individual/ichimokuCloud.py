import numpy as np


def ichimokuCloud(df):
    """
    A versatile indicator that provides information on support and resistance levels, trend direction, and momentum.
    df: dataframe
    """ 
    try:    
        
        # Define the period for the Stochastic Oscillator
        tenkan_period = 9
        kijun_period = 26
        senkou_b_period = 52

        # Calculate the Tenkan Sen (Conversion Line)
        df['Tenkan_Sen'] = (df['High'].rolling(window=tenkan_period).max() + df['Low'].rolling(window=tenkan_period).min()) / 2

        # Calculate the Kijun Sen (Base Line)
        df['Kijun_Sen'] = (df['High'].rolling(window=kijun_period).max() + df['Low'].rolling(window=kijun_period).min()) / 2

        # Calculate the Senkou Span A (Leading Span A)
        df['Senkou_Span_A'] = ((df['Tenkan_Sen'] + df['Kijun_Sen']) / 2).shift(kijun_period)

        # Calculate the Senkou Span B (Leading Span B)
        df['Senkou_Span_B'] = ((df['High'].rolling(window=senkou_b_period).max() + df['Low'].rolling(window=senkou_b_period).min()) / 2).shift(kijun_period)

        # Calculate the Kumo (Cloud)
        df['Kumo'] = np.where(df['Senkou_Span_A'] > df['Senkou_Span_B'], 'Bullish', 'Bearish')

        return df
    
    except Exception as e:
        print(f"An error occurred in ichimokuCloud.py: {str(e)}")

    

    