import os
import sys

sys.path.append(os.environ.get("INSTALL_FOLDER_ORB"))


from src.modules.preprocess.copydataset import copy_files

from src.modules.process.getColumnsDone import getColumnsDone

from src.modules.process.individual.processIndividualParameters import processIndividualParameters
from src.modules.process.individual.appendBTCPrice import appendBTCPrice
from src.modules.process.individual.createPercentChange import createPercentChange

src = os.path.join(os.getcwd(), "dataset", "raw")
des = os.path.join(os.getcwd(), "dataset", "temp_raw")


copy_files(src, des)

processIndividualParameters(des)



