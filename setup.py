#!/usr/bin/env python3

import sys
from setuptools import setup, find_packages, Command

# Package meta-data
VERSION = '0.22.0'
CORE_VERSION = '0.22.0'  # graphANNIS core library version


class CoreLibraryCommand(Command):
    """Download released graphANNIS core library binaries"""

    description = 'Download released graphANNIS core library binaries'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.status('Downloading released graphANNIS ' +
                    VERSION + ' core library binaries')

        sys.exit()


with open('README_pypi.md') as f:
    long_description = f.read()

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
      cmdclass={
          'build_clib': CoreLibraryCommand
      }
      )
