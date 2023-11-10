import shutil
import os

import pandas as pd

from .modules.copydataset import copydataset
from .modules.addCoinName import addCoinName
from .modules.marketReturn import marketReturn


def preProcess(src,temp_raw,marketOutput):
    """
    This Function runs all preprocess modules
    """
    try:

        output_directory = os.path.dirname(marketOutput)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)


        copydataset(src, temp_raw)
        addCoinName(temp_raw)
        marketReturn(temp_raw,marketOutput)

        print(f"Successful preProcess.py")

    except Exception as e:
        print(f"An error occurred in preProcess.py: {str(e)}")
