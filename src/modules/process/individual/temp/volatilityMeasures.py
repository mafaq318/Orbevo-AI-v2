import numpy as np

def volatilityMeasures(df):
    """
    Calculate standard deviation, average true range (ATR), or historical volatility to assess the level of price volatility.
    df: dataframe
    """ 
    try:    

        window = 20
        df['Price_STD'] = df['Close'].rolling(window=window).std()

        df['TR'] = df['High'] - df['Low']
        df['HL'] = abs(df['High'] - df['Close'].shift(1))
        df['LH'] = abs(df['Low'] - df['Close'].shift(1))
        df['TR'] = df[['TR', 'HL', 'LH']].max(axis=1)
        df['ATR'] = df['TR'].rolling(window=window).mean()

        df['LogReturns'] = np.log(df['Close'] / df['Close'].shift(1))
        df['HistoricalVolatility'] = df['LogReturns'].rolling(window=window).std() * (252 ** 0.5)
        
        df = df.drop(['TR', 'HL','LH','TR','LogReturns'], axis=1)

        return df
    
    except Exception as e:
        print(f"An error occurred in volatilityMeasures.py: {str(e)}")

    

    