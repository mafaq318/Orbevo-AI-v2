
def volumeChange(df,vroc_period):
    """
    Compute Volume Change compared to last date
    df: dataframe
    """ 
    try:
        
        df['Volume_Change'] = (df['Volume'] / df['Volume'].shift(vroc_period) - 1) * 100

        return df
    
    except Exception as e:
        print(f"An error occurred in volumeChange.py: {str(e)}")

    

    