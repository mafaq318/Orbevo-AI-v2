import os
import sys
import shutil

sys.path.append(os.environ.get("INSTALL_FOLDER_ORB"))


from src.modules.preprocess.preProcess import preProcess

from src.modules.process.processIndividualParameters import processIndividualParameters

from src.modules.postprocess.joinIndividualFiles import joinIndividualFiles


remove_temp = False

src = os.path.join(os.getcwd(), "dataset", "raw")
temp_raw = os.path.join(os.getcwd(), "dataset", "temp_raw")

marketReturn = os.path.join(os.getcwd(), "dataset", "temp_raw","helper","marketReturn.csv")
TrainData = os.path.join(os.getcwd(), "dataset", "TrainData","XData.csv")

preProcess(src,temp_raw,marketReturn)

#processIndividualParameters(temp_raw)
#joinIndividualFiles(temp_raw,TrainData)

if(remove_temp):
    shutil.rmtree(temp_raw)

