import os
import pandas as pd 
from alive_progress import alive_bar
def getColumnsDone(src_file,des):
    """
    Read Temp Data files and Find out which columns are available. 
    src_file = File whose columns to be extracted
    des = folder where to save columns/columns.csv
    """ 

    try:
        df = pd.read_csv(src_file)
        column_names = df.columns
        if not os.path.exists(os.path.join(des, "columns/columns.csv")):
            os.makedirs(os.path.join(des, "columns"))
        file_path = os.path.join(des, "columns/columns.csv")
        column_names.to_frame().to_csv(file_path, index=False, header=False)
    
    except Exception as e:
        print(f"An error occurred in getColumnsDone.py: {str(e)}")

    

    