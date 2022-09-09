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

echo "running flake8"
flake8 . --config ./flake8_config
echo "flake8 has been run if you do not see anything this means flake8 is completely satisfied"
