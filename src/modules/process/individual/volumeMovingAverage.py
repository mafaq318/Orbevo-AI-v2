
def volumeMovingAverage(df,window):
    """
    Computes simple moving average of Volume
    sums up "Close" values over window and divides by N. Later normalizes it.
    df: dataframe
    """ 
    try:
        
        VMA_Column = 'VMA{}'.format(window)
        VMA_Norm_Column = 'Normalized_VMA_{}'.format(window)

        df[VMA_Column] = df['Volume'].rolling(window=window).mean()

        # Normalize the VMA values to the range [0, 1]
        min_vma = df[VMA_Column].min()
        max_vma = df[VMA_Column].max()

        df[VMA_Norm_Column] = (df[VMA_Column] - min_vma) / (max_vma - min_vma)
        df = df.drop(VMA_Column, axis=1)

        return df
    
    except Exception as e:
        print(f"An error occurred in volumeMovingAverage.py: {str(e)}")

    

    