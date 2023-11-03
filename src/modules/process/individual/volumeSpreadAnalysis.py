
def volumeSpreadAnalysis(df):
    """
    VSA combines price and volume analysis to identify the activity of professional traders (smart money) and retail traders (dumb money). It helps in understanding market manipulation and potential trend reversals.
    df: dataframe
    """ 
    try:
        
        #Calculate the short-term volume moving average
        df['Spread'] = df['High'] - df['Low']
        df['PriceChange'] = df['Close'].diff()
        df['VolumeChange'] = df['Volume'].diff()

        # Signal: Climax Buying (CB)
        # If price goes up and volume increases, it might indicate Climax Buying
        df['VSA_CB_Signal'] = (df['PriceChange'] > 0) & (df['VolumeChange'] > 0)

        # Signal: Climax Selling (CS)
        # If price goes down and volume increases, it might indicate Climax Selling
        df['VSA_CS_Signal'] = (df['PriceChange'] < 0) & (df['VolumeChange'] > 0)

        df = df.drop(['Spread', 'PriceChange','VolumeChange'], axis=1)

        return df
    
    except Exception as e:
        print(f"An error occurred in volumeSpreadAnalysis.py: {str(e)}")

    

    