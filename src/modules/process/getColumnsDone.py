import os
import pandas as pd 
from progress.spinner import MoonSpinner

def getColumnsDone(folder):
    """
    Read Temp Data files and Find out which columns are available. 
    folder = directory which contains are csv files.
    """ 

    try:
        if not os.path.exists(folder):
            raise FileNotFoundError(f"error: directory '{folder}' not found")
        
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f.endswith('.csv')]

        if not files:
            raise FileNotFoundError(f"error: No csv files found in '{folder}'")
        

        column_sets = []
        prev_column_set = []
        with MoonSpinner('Exporting Columns to Column.csv under ${des} ...') as bar:
            for file in files:
                file_path = os.path.join(folder, file)
                df = pd.read_csv(file_path)
                column_set = set(df.columns)
                column_sets.append((file, column_set))
                bar.next()
        
        print(type(column_sets));
        #unique_column_sets = set(column_sets)
        #if len(unique_column_sets) == 1:
        #    print("All files have the same columns.")
        #    print(unique_column_sets)
        #else:
        #    print("Error: Files have different columns.")
        #    print("Column sets across files:")
        #    for file, column_set in column_sets:
        #        print(f"{file}: {column_set}")
        #    raise ValueError(f'ERROR')
    
    except Exception as e:
        print(f"An error occurred in getColumnsDone.py: {str(e)}")

    

    