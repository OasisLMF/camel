#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH
cd ..

if [ ! -d "./venv" ]
then
    echo "venv does not exist, creating venv"
    python3 -m venv venv
    pip install requests==2.28.1
    pip install termcolor
    pip install pyyaml
fi

source venv/bin/activate
export PYTHONPATH="."

python -m unittest
