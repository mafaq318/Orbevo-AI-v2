import os
import pandas as pd 
import numpy as np

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
from .individual.volumeSpreadAnalysis import volumeSpreadAnalysis
from .individual.climaxBuying import climaxBuying
from .individual.volumeDivergence import volumeDivergence
from .individual.A_D_Line import A_D_Line
from .individual.supportResistance import supportResistance
from .individual.volatilityMeasures import volatilityMeasures
from .individual.stochasticOscillator import stochasticOscillator
from .individual.ichimokuCloud import ichimokuCloud

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

            

                df = df.fillna(0)
                df.replace([np.inf, -np.inf], 0, inplace=True)
                df.to_csv(file_path, index=False) 
                bar()

        getColumnsDone(BTC_Path,folder)
    
    except Exception as e:
        print(f"An error occurred in processIndividualParameters.py: {str(e)}")

    

    