
def volumeRelative(df,average_volume_period):
    """
    This metric compares the current trading volume to the average volume over a specific period. Higher-than-average volume can indicate increased interest in an asset.
    df: dataframe
    """ 
    try:
        
        # Calculate the average volume over the specified period
        df['Average_Volume'] = df['Volume'].rolling(window=average_volume_period).mean()

        # Calculate the Relative Volume
        df['Relative_Volume'] = df['Volume'] / df['Average_Volume']


        return df
    
    except Exception as e:
        print(f"An error occurred in volumeRelative.py: {str(e)}")

    

    