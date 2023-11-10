import os
import shutil


Path_to_Temp = os.path.join(os.getcwd(), "dataset", "temp_raw")
Path_to_TrainData = os.path.join(os.getcwd(), "dataset", "TrainData")

print('Doing Cleanup of repo')

try:
    if os.path.exists(Path_to_Temp):
        shutil.rmtree(Path_to_Temp)
 
    if os.path.exists(Path_to_TrainData):
        shutil.rmtree(Path_to_TrainData)

except Exception as e:
        print(f"An error occurred in appendBTCPrice.py: {str(e)}")


print('Cleanup done')
