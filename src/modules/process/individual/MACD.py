
def MACD(df,long_term_period, short_term_period, signal_period):
    """
    Computes Moving Average Convergence Divergence primarily used to identify potential changes in the direction of an asset's price and to gauge the strength of a trend
    df: dataframe
    long_term_period: to calculate long term EMA
    short_term_period: to calculate short term EMA
    signal_period: to calculate signal line

    """ 
    try:    
        # Calculate the short-term EMA
        df['short_ema'] = df['Close'].ewm(span=short_term_period, adjust=False).mean()

        # Calculate the long-term EMA
        df['long_ema'] = df['Close'].ewm(span=long_term_period, adjust=False).mean()

        # Calculate the MACD line
        df['macd'] = df['short_ema'] - df['long_ema']

        # Define the signal period
        signal_period = 9

        # Calculate the signal line (9-period EMA of the MACD)
        df['macd_signal_line'] = df['macd'].ewm(span=signal_period, adjust=False).mean()

        # Calculate the MACD histogram
        df['macd_histogram'] = df['macd'] - df['macd_signal_line']

        df = df.drop(['short_ema', 'long_ema', 'macd'], axis=1)
        
        return df
    
    except Exception as e:
        print(f"An error occurred in MACD.py: {str(e)}")

    

    