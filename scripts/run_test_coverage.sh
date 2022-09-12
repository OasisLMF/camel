#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH
cd ..

if [ ! -d "./venv" ]
then
    echo "venv does not exist, creating venv"
    python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH="."

python -m coverage run -m unittest
python -m coverage report
