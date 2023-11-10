
def RSI(df,period):
    """
    Computes RSI to measure oversold or overbought condition
    df: dataframe
    """ 
    try:    

        delta = df['Close'].diff(1)
    
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        average_gain = gain.rolling(period).mean()
        average_loss = loss.rolling(period).mean()

        rs = average_gain / average_loss

        df['RSI']  = 100 - (100 / (1 + rs))
        
        return df
    
    except Exception as e:
        print(f"An error occurred in RSI.py: {str(e)}")

    

    