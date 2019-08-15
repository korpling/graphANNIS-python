#!/usr/bin/env python3

import sys
from setuptools import setup, find_packages
from distutils.command.clean import clean as clean_orig
import urllib.request
import shutil
import os
import os.path

# Package meta-data
VERSION = '0.22.0'
CORE_VERSION = '0.22.0'  # graphANNIS core library version


with open('README_pypi.md') as f:
    long_description = f.read()


CORE_FILES = {
    'linux-x86-64/libgraphannis.so': 'https://github.com/korpling/graphANNIS/releases/download/v' +
    CORE_VERSION + '/libgraphannis.so',
    'win32-x86-64/graphannis.dll': 'https://github.com/korpling/graphANNIS/releases/download/v' +
    CORE_VERSION + '/graphannis.dll',
    'darwin-x86-64/libgraphannis.dylib': 'https://github.com/korpling/graphANNIS/releases/download/v' +
    CORE_VERSION + '/libgraphannis.dylib'
}



if not "clean" in sys.argv:
  for file, url in CORE_FILES.items():
        file = os.path.join('graphannis', file)
        if not os.path.isfile(file):
            print("Downloading " + url)
            with urllib.request.urlopen(url) as response, open(file, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)

class clean(clean_orig):

    def run(self):
        for file, _ in CORE_FILES.items():
            file = os.path.join("graphannis", file)
            if os.path.isfile(file):
                print(file)
                os.remove(file)
        super().run()


setup(name='graphannis',
      version=VERSION,
      description='graphANNIS Python API',
      author='Thomas Krause',
      author_email='thomaskrause@posteo.de',
      url='https://github.com/korpling/graphANNIS-python/',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['graphannis'],
      include_package_data=True,
      setup_requires=["cffi>=1.0.0"],
      cffi_modules=["package/graphannis_build.py:ffibuilder"],
      install_requires=["cffi>=1.0.0", "networkx"],
      classifiers=(
          "Programming Language :: Python :: 3.6",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: POSIX :: Linux",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows"
      ),
      cmdclass={"clean": clean}
      )
