import os
import sys
import shutil

sys.path.append(os.environ.get("INSTALL_FOLDER_ORB"))


from src.modules.preprocess.copydataset import copy_files
from src.modules.preprocess.addCoinName import addCoinName

from src.modules.process.processIndividualParameters import processIndividualParameters

from src.modules.postprocess.joinIndividualFiles import joinIndividualFiles


remove_temp = True

src = os.path.join(os.getcwd(), "dataset", "raw")
temp_raw = os.path.join(os.getcwd(), "dataset", "temp_raw")
TrainData = os.path.join(os.getcwd(), "dataset", "TrainData","XData.csv")

copy_files(src, temp_raw)
addCoinName(temp_raw)
processIndividualParameters(temp_raw)
joinIndividualFiles(temp_raw,TrainData)

if(remove_temp):
    shutil.rmtree(temp_raw)

