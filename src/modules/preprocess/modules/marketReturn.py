import shutil
import os

import pandas as pd

def marketReturn(folder_path, market_return_output):
    """
    This Function creates a market Return Csv
    """
    try:
        market_return_df = pd.DataFrame(columns=['Date','Asset_Return'])

        # Iterate through each CSV file in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(folder_path, filename)
                try:
                    asset_df = pd.read_csv(file_path)
                except pd.errors.EmptyDataError:
                    # Handle empty file or other read errors
                    print(f"Error reading {file_path}. Skipping...")
                    continue

                asset_df[f'Asset_Return'] = (asset_df['Close'] - asset_df['Open']) / asset_df['Open']
                asset_df['Asset_Return'].fillna(0, inplace=True)
                asset_df.drop(['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume',
       'Coin_Name'], axis=1, inplace=True)
                market_return_df = pd.concat([market_return_df, asset_df])
        
        market_return_df['Date'] = pd.to_datetime(market_return_df['Date'])
        market_return_df = market_return_df.groupby('Date')['Asset_Return'].mean().reset_index()        

        # Save the market return DataFrame to a new CSV file
        market_return_df.to_csv(market_return_output, index=False)

        print(f"Successful marketReturn.py")

    except Exception as e:
        print(f"An error occurred in marketReturn.py: {str(e)}")
