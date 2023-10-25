
def exponentialMovingAverage(df,span,bias):
    """
    Computes Exponential Moving Average
    df: dataframe
    """ 
    try:    

        EMA_Column = 'EMA_{}'.format(span)
        EMA_Norm_Column = 'Normalized_EMA_{}'.format(span)
        
        df[EMA_Column] = df['Close'].ewm(span=span, adjust=bias).mean()
        min_ema = df[EMA_Column].min()
        max_ema = df[EMA_Column].max()
        df[EMA_Norm_Column] = (df[EMA_Column] - min_ema) / (max_ema - min_ema)

        df[EMA_Column].fillna(0, inplace=True)
        df[EMA_Norm_Column].fillna(0, inplace=True)
        df = df.drop(EMA_Column, axis=1)
        return df
    
    except Exception as e:
        print(f"An error occurred in exponentialMovingAverage.py: {str(e)}")

    

    