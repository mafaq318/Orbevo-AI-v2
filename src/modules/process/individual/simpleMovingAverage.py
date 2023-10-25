
def simpleMovingAverage(df,window):
    """
    Computes simple moving average
    sums up "Close" values over window and divides by N. Later normalizes it.
    df: dataframe
    """ 
    try:
        
        SMA_Column = 'SMA_{}'.format(window)
        SMA_Norm_Column = 'Normalized_SMA_{}'.format(window)

        df[SMA_Column] = df['Close'].rolling(window=window).mean()
        
        min_sma = df[SMA_Column].min()
        max_sma = df[SMA_Column].max()
        df[SMA_Norm_Column] = (df[SMA_Column] - min_sma) / (max_sma - min_sma)

        df[SMA_Column].fillna(0, inplace=True)
        df[SMA_Norm_Column].fillna(0, inplace=True)
        
        df = df.drop(SMA_Column, axis=1)

        return df
    
    except Exception as e:
        print(f"An error occurred in simpleMovingAverage.py: {str(e)}")

    

    