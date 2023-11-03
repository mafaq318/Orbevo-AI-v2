
def bollingerBands(df, num_std_dev, window):
    """
    Computes Bollinger bands to measure volatility
    df: dataframe
    """ 
    try:
        
        df['Bollinger_Middle_Band'] = df['Close'].rolling(window=window).mean()
        df['Bollinger_Middle_Std_Dev'] = df['Close'].rolling(window=window).std()

        #df['Bollinger_Upper_Band'] = df['Normalized_SMA_20'] + (num_std_dev * df['Bollinger_Middle_Std_Dev'])
        #df['Bollinger_Lower_Band'] = df['Normalized_SMA_20'] - (num_std_dev * df['Bollinger_Middle_Std_Dev'])

        df['Bollinger_Upper_Band'] = df['SMA_20'] + (num_std_dev * df['Bollinger_Middle_Std_Dev'])
        df['Bollinger_Lower_Band'] = df['SMA_20'] - (num_std_dev * df['Bollinger_Middle_Std_Dev'])

        df['Bollinger_Upper_Band'] = (df['Bollinger_Upper_Band'] - df['Bollinger_Lower_Band'].min()) / (df['Bollinger_Upper_Band'].max() - df['Bollinger_Lower_Band'].min())
        df['Bollinger_Middle_Band'] = (df['Bollinger_Middle_Band'] - df['Bollinger_Lower_Band'].min()) / (df['Bollinger_Upper_Band'].max() - df['Bollinger_Lower_Band'].min())
        df['Bollinger_Lower_Band'] = (df['Bollinger_Lower_Band'] - df['Bollinger_Lower_Band'].min()) / (df['Bollinger_Upper_Band'].max() - df['Bollinger_Lower_Band'].min())

        return df
    
    except Exception as e:
        print(f"An error occurred in bollingerBands.py: {str(e)}")

    

    