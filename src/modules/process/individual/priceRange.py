
def priceRange(df):
    """
    Compute price range in terms of movement. High-Low / Open
    df: dataframe
    """ 
    try:
        
        if 'PriceRangeHigh' not in df.columns:
            df['PriceRangeHigh'] = (df['High'] - df['Open']) / df['Open']
        
        if 'PriceRangeLow' not in df.columns:
            df['PriceRangeLow'] = (df['Low'] - df['Open']) / df['Open']
        
        df = df.fillna(0)
        return df
    
    except Exception as e:
        print(f"An error occurred in priceRange.py: {str(e)}")

    

    