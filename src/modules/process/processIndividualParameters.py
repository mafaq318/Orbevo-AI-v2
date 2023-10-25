import os
import pandas as pd 
from alive_progress import alive_bar

from .individual.appendBTCPrice import appendBTCPrice
from .individual.createPercentChange import createPercentChange
from .individual.priceRange import priceRange
from .individual.volumeChange import volumeChange
from .individual.simpleMovingAverage import simpleMovingAverage
from .individual.exponentailMovingAverage import exponentialMovingAverage
from .individual.bollingerBands import bollingerBands
from .individual.RSI import RSI
from .individual.MACD import MACD
from .individual.volumeMovingAverage import volumeMovingAverage
from .individual.OBV import OBV
from .individual.volumeOscillator import volumeOscillator
from .individual.volumeRelative import volumeRelative

from .getColumnsDone import getColumnsDone
def processIndividualParameters(folder, calculate_BTC_price_change = True):
    """
    Loops over the files in the folder and adds individual parameter columns to each csv.
    """ 

    try:
        if not os.path.exists(folder):
            raise FileNotFoundError(f"error: directory '{folder}' not found")
        
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f.endswith('.csv')]
        BTC_Path = os.path.join(folder, "BTC_Bitcoin.csv")

        if not files:
            raise FileNotFoundError(f"error: No csv files found in '{folder}'")
        
        if not os.path.exists(BTC_Path):
            raise FileNotFoundError(f"error: No BTC_Bitcoin csv file found in '{folder}'")
        
        BTC_df = pd.read_csv(BTC_Path)
        
        print(f"Processing individual Parameters on '{folder}")
        with alive_bar(len(files), bar = 'bubbles', spinner = 'notes2') as bar:
            for file in files:
                file_path = os.path.join(folder, file)
                df = pd.read_csv(file_path)

                df = appendBTCPrice(df,BTC_df)
                df = createPercentChange(df,calculate_BTC_price_change)
                df = priceRange(df)

                Volume_change_period = 2
                df = volumeChange(df,Volume_change_period)
                df = OBV(df)

                short_period = 3
                long_period = 5
                df = volumeOscillator(df,short_period,long_period)

                average_volume_period = 3
                df = volumeRelative(df,average_volume_period)

                df = volumeMovingAverage(df,5)
                df = volumeMovingAverage(df,20)
                df = volumeMovingAverage(df,50)
                df = volumeMovingAverage(df,100)
                df = volumeMovingAverage(df,200)


                df = simpleMovingAverage(df,5)
                df = simpleMovingAverage(df,20)
                df = simpleMovingAverage(df,50)
                df = simpleMovingAverage(df,100)
                df = simpleMovingAverage(df,200)
                

                EMA_Bias = True
                df = exponentialMovingAverage(df,5,EMA_Bias)
                df = exponentialMovingAverage(df,20,EMA_Bias)
                df = exponentialMovingAverage(df,50,EMA_Bias)
                df = exponentialMovingAverage(df,100,EMA_Bias)
                df = exponentialMovingAverage(df,200,EMA_Bias)

                num_std_bollinger = 2
                Bollinger_window = 20
                df = bollingerBands(df,num_std_bollinger,Bollinger_window)

                RSI_Window = 14
                df = RSI(df,RSI_Window)

                long_term_period = 26
                short_term_period = 13
                signal_period = 9
                df = MACD(df,long_term_period, short_term_period, signal_period)


                df = df.fillna(0)
                df.to_csv(file_path, index=False) 
                bar()

        getColumnsDone(BTC_Path,folder)
    
    except Exception as e:
        print(f"An error occurred in processIndividualParameters.py: {str(e)}")

    

    