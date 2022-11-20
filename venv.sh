#!/bin/sh

if [ ! -f venv/bin/activate ]
then
    echo "Creating venv ..."
    python3 -m venv venv
fi

echo "Activating venv ..."
. venv/bin/activate

which python
python --version

echo "Updating pip ..."
python -m pip install --upgrade pip

echo "Updating tools ..."
pip install wheel
pip install setuptools
pip install twine

pip install pytest
pip install pytest-runner
pip install flake8

echo "Updating requirements ..."
pip install -r requirements.txt
