
def A_D_Line(df):
    """
        This indicator tracks the accumulation or distribution of an asset by comparing the closing price with the trading range. It helps identify potential trend changes.
        df: dataframe
    """ 
    try:
        
        df['Money_Flow_Volume'] = ((df['Close'] - df['Low']) - (df['High'] - df['Close'])) / (df['High'] - df['Low']) * df['Volume']
        df['A/D_Line'] = df['Money_Flow_Volume'].cumsum()

       # df = df.drop(['Money_Flow_Volume'], axis=1)
        return df
    
    except Exception as e:
        print(f"An error occurred in A_D_Line.py: {str(e)}")

    

    