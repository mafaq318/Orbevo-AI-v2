
def climaxBuying(df):
    """
        Climax volume refers to unusually high trading volume, often at the end of a trend. It can signal a potential reversal or continuation of the current trend.
        df: dataframe
    """ 
    try:
        
        threshold = 3 * df['Volume'].rolling(3).mean()  # You can adjust the threshold as needed

        # Identify Climax Volume based on the threshold
        df['Climax_Volume'] = (df['Volume'] > threshold).astype(int)

        return df
    
    except Exception as e:
        print(f"An error occurred in climaxBuying.py: {str(e)}")

    

    