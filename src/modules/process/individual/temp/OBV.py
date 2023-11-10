
def OBV(df):
    """
    Computes OBV a cumulative indicator that adds or subtracts volume based on whether the closing price is higher or lower than the previous day.
    df: dataframe
    """ 
    try:    

        df['OBV'] = 0  
        price_diff = df['Close'].diff()
        df.loc[price_diff > 0, 'OBV'] = df['Volume']
        df.loc[price_diff < 0, 'OBV'] = -df['Volume']

        return df
    
    except Exception as e:
        print(f"An error occurred in OBV.py: {str(e)}")

    

    