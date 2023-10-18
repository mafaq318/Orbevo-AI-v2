
def appendBTCPrice(df, BTC_df):
    """
    Read Data file and Append columns open,close,high,low and market cap of BTC with the coins df.
    df: dataframe
    """ 
    try:
        if any(col.endswith('_BTC') for col in df.columns):
            pass
        else:
            df = df.merge(BTC_df, on='Date', suffixes=('', '_BTC'))
            df = df.fillna(0)
    
        return df
    
    except Exception as e:
        print(f"An error occurred in appendBTCPrice.py: {str(e)}")

    

    