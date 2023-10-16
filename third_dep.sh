#!/bin/sh

sudo apt-get install python3-venv

python3 -m venv env
source env/bin/activate

sudo apt-get install python3 python-is-python3 