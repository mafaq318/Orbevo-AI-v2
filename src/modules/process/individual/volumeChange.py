
def volumeChange(df):
    """
    Compute Volume Change compared to last date
    df: dataframe
    """ 
    try:
        
        df['Volume_Change'] = (df['Volume'] - df['Volume'].shift(1)) / df['Volume'].shift(1)
        df['Volume_Change'].fillna(0, inplace=True)

        return df
    
    except Exception as e:
        print(f"An error occurred in volumeChange.py: {str(e)}")

    

    