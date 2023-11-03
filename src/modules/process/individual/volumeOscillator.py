
def volumeOscillator(df,short_period,long_period):
    """
    The volume oscillator is used to identify potential turning points and divergence between price and volume.
    df: dataframe
    """ 
    try:
        
        #Calculate the short-term volume moving average
        df['Short_VMA'] = df['Volume'].rolling(window=short_period).mean()

        # Calculate the long-term volume moving average
        df['Long_VMA'] = df['Volume'].rolling(window=long_period).mean()

        # Calculate the Volume Oscillator
        df['Volume_Oscillator'] = df['Short_VMA'] - df['Long_VMA']

        min_value = df['Volume_Oscillator'].min()
        max_value = df['Volume_Oscillator'].max()

        df['Normalized_Volume_Oscillator'] = (df['Volume_Oscillator'] - min_value) / (max_value - min_value)
        df = df.drop(['Short_VMA', 'Long_VMA','Volume_Oscillator'], axis=1)

        return df
    
    except Exception as e:
        print(f"An error occurred in volumeOscillator.py: {str(e)}")

    

    