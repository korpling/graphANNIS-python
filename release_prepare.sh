#!/bin/bash

echo "Building package and downloading release binaries"
python3 setup.py clean
python3 setup.py build
echo "Running unit tests"
python3 -m unittest
echo "Running documentation tests"
./doctest_runner.py
echo "Updating changelog header"
python3 ./package/update_changelog.py