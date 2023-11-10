
def priceRange(df):
    """
    Compute price range in terms of movement. High-Low / Open
    df: dataframe
    """ 
    try:
        
        df['PriceRangeHigh'] = (df['High'] - df['Open']) / df['Open']
    
        df['PriceRangeLow'] = (df['Low'] - df['Open']) / df['Open']

        df['PriceRangeHigh_BTC'] = (df['High_BTC'] - df['Open_BTC']) / df['Open_BTC']
    

        df['PriceRangeLow_BTC'] = (df['Low_BTC'] - df['Open_BTC']) / df['Open_BTC']
        
        return df
    
    except Exception as e:
        print(f"An error occurred in priceRange.py: {str(e)}")

    

    