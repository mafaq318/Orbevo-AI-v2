
def createPercentChange(df , BTC):
    """
    Read CSV Data file and append columns Percent_Change = (close-open)/open
    df: dataframe
    BTC : True or False. Calculate BTC change columns as well 
    """ 

    try:
        
        if '24hChange' not in df.columns:
            df['24hChange'] = (df['Close'] - df['Open']) / df['Open']
            
        if(BTC == True):
            if '24hChange_BTC' not in df.columns:
                df['24hChange_BTC'] = (df['Close_BTC'] - df['Open_BTC']) / df['Open_BTC']
        
        return df
    
    except Exception as e:
        print(f"An error occurred in createPercentChange.py: {str(e)}")

    

    