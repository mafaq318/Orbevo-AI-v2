import os
import sys

sys.path.append(os.environ.get("INSTALL_FOLDER_ORB"))

from src.modules.process.appendBTCPrice import appendBTCPrice
from src.modules.preprocess.copydataset import copy_files

src = os.path.join(os.getcwd(), "dataset", "raw")
des = os.path.join(os.getcwd(), "dataset", "temp_raw")

copy_files(src, des)

appendBTCPrice(des)
