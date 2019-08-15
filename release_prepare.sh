#!/bin/bash

python3 setup.py clean
python3 setup.py build
python3 -m unittest
./doctest_runner.py
python3 ./package/update_changelog.py