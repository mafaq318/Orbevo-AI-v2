
def volumeDivergence(df):
    """
        This occurs when the price and volume move in opposite directions. It may suggest a weakening trend or an upcoming reversal.
        df: dataframe
    """ 
    try:
        
        df['PriceChange'] = df['Close'].diff()
        df['VolumeChange'] = df['Volume'].diff()

        # Identify Volume Divergence
        df['Volume_Divergence'] = (df['PriceChange'] > 0) & (df['VolumeChange'] < 0) | (df['PriceChange'] < 0) & (df['VolumeChange'] > 0)

        # Convert Volume Divergence to 0 and 1

        
        df['Volume_Divergence'] = df['Volume_Divergence'].astype(int)

        df = df.drop(['PriceChange', 'VolumeChange'], axis=1)
        return df
    
    except Exception as e:
        print(f"An error occurred in volumeDivergence.py: {str(e)}")

    

    