import os
import shutil


Path_to_Temp = os.path.join(os.getcwd(), "dataset", "temp_raw")

print('Doing Cleanup of repo')

try:
    shutil.rmtree(Path_to_Temp)
except FileNotFoundError:
    print(f"Cleanup Error : File not found: {Path_to_Temp}")


print('Cleanup done')
