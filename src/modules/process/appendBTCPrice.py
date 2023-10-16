import os
import pandas as pd 
from progress.spinner import MoonSpinner

def appendBTCPrice(folder):
    """
    Read Temp Data files and append columns open,close,high,low and market cap of BTC with each. 
    folder = directory which contains are csv files.
    """ 

    try:
        if not os.path.exists(folder):
            raise FileNotFoundError(f"error: directory '{folder}' not found in appendBTCPrice")
        
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f.endswith('.csv')]
        BTC_Path = os.path.join(folder, "BTC_Bitcoin.csv")

        if not files:
            raise FileNotFoundError(f"error: No csv files found in '{folder}'")
        
        if not os.path.exists(BTC_Path):
            raise FileNotFoundError(f"error: No BTC_Bitcoin csv file found in '{folder}'")
        
        BTC_df = pd.read_csv(BTC_Path)

        with MoonSpinner('Appending BTC values...') as bar:
            for file in files:
                file_path = os.path.join(folder, file)
                df = pd.read_csv(file_path)
                df_columns= set(df.columns)

                if any(col.endswith('_BTC') for col in df_columns):
                    pass
                else:
                    df = df.merge(BTC_df, on='Date', suffixes=('', '_BTC'))
                    df = df.fillna(0)
                    df.to_csv(file_path, index=False) 
                bar.next()
    
    except Exception as e:
        print(f"An error occurred in appendBTCPrice.py: {str(e)}")

    

    