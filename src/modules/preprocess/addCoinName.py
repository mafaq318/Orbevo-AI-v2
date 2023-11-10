import shutil
import os

import pandas as pd

def addCoinName(folder_path):
    """
    This Function adds the coin name under the column Coin_Name.
    """
    try:
        csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

        for file in csv_files:
            file_path = os.path.join(folder_path, file)

            df = pd.read_csv(file_path)

            coin_name = file.replace('.csv', '')

            df['Coin_Name'] = coin_name

            df.to_csv(file_path, index=False)

        print(f"Successful addCoinName.py")

    except Exception as e:
        print(f"An error occurred in addCoinName.py: {str(e)}")
