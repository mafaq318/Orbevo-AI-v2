import os
import pandas as pd 
from alive_progress import alive_bar


def joinIndividualFiles(folder_path, output_file):
    """
    This functions joins all coin.csvs into one single file
    """
    try:
        # Get a list of all CSV files in the specified folder
        csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

        # Check if there are any CSV files
        if not csv_files:
            print("No CSV files found in the specified folder.")
            return

        # Initialize an empty DataFrame to store the concatenated data
        concatenated_data = pd.DataFrame()

        print("Initialising XData for Training")
        # Iterate through each CSV file and concatenate the data
        with alive_bar(len(csv_files), bar = 'bubbles', spinner = 'notes2') as bar:
            for csv_file in csv_files:
                file_path = os.path.join(folder_path, csv_file)
                data = pd.read_csv(file_path)
                concatenated_data = pd.concat([concatenated_data, data], ignore_index=True)
                bar()

        # Write the concatenated data to the output CSV file
        output_directory = os.path.dirname(output_file)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        

        concatenated_data.to_csv(output_file, index=False)
        print(f"Data successfully concatenated and saved to {output_file}.")

    except Exception as e:
        print(f"An error occurred in joinIndividualFiles: {str(e)}")



