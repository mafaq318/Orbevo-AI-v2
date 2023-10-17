#!/bin/sh

export INSTALL_FOLDER_ORB=$(dirname "$(realpath "$0")")

#python src/modules/run/cleanup.py
python src/modules/run/run.py