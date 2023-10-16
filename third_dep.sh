#!/bin/sh

sudo apt-get install python3 python-is-python3 python3-venv

python3 -m venv env

. env/bin/activate

pip install -r requirements.txt


