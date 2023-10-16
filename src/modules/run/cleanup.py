import os
import shutil


Path_to_Temp = os.path.join(os.getcwd(), "dataset", "temp_raw")

print('Doing Cleanup of repo')

try:
    if os.path.exists(Path_to_Temp):
        shutil.rmtree(Path_to_Temp)

except Exception as e:
        print(f"An error occurred in appendBTCPrice.py: {str(e)}")


print('Cleanup done')
