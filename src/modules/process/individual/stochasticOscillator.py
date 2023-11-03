def stochasticOscillator(df):
    """
    Calculate standard deviation, average true range (ATR), or historical volatility to assess the level of price volatility.
    df: dataframe
    """ 
    try:    
        
        # Define the period for the Stochastic Oscillator
        k_period = 14  # %K period
        d_period = 3   # %D period

        df['L14'] = df['Low'].rolling(window=k_period).min()
        df['H14'] = df['High'].rolling(window=k_period).max()
        df['%K'] = (df['Close'] - df['L14']) / (df['H14'] - df['L14']) * 100
        df['%D'] = df['%K'].rolling(window=d_period).mean()
        
        df = df.drop(['L14', 'H14'], axis=1)

        return df
    
    except Exception as e:
        print(f"An error occurred in stochasticOscillator.py: {str(e)}")

    

    