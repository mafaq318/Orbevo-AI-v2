
def supportResistance(df):
    """
    Identify price levels where the asset historically found support or resistance and consider their relevance in the current context.
    df: dataframe
    """ 
    try:    

        df['Pivot'] = (df['High'] + df['Low'] + df['Close']) / 3

        # Calculate the first support level
        df['Support1'] = (2 * df['Pivot']) - df['High']

        # Calculate the second support level
        df['Support2'] = df['Pivot'] - (df['High'] - df['Low'])

        # Calculate the third support level
        df['Support3'] = df['Low'] - 2 * (df['High'] - df['Pivot'])

        # Calculate the first resistance level
        df['Resistance1'] = (2 * df['Pivot']) - df['Low']

        # Calculate the second resistance level
        df['Resistance2'] = df['Pivot'] + (df['High'] - df['Low'])

        # Calculate the third resistance level
        df['Resistance3'] = df['High'] + 2 * (df['Pivot'] - df['Low'])

        
        return df
    
    except Exception as e:
        print(f"An error occurred in supportResistance.py: {str(e)}")

    

    