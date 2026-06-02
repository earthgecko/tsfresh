# -*- coding: utf-8 -*-
"""
    Setup file for tsfresh.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.2.3.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import sys

# @modified 20260211 - Branch #5706: v0.21.91
# pkg_resources API deprecated
#from pkg_resources import VersionConflict, require
from setuptools import setup

# @modified 20260211 - Branch #5706: v0.21.91
# pkg_resources API deprecated
#try:
#    require("setuptools>=38.3")
#except VersionConflict:
#    print("Error: version of setuptools is too old (<38.3)!")
#    sys.exit(1)


if __name__ == "__main__":
# @modified 20260211 - Branch #5706: v0.21.91
# Remove pyscaffold
#    setup(use_pyscaffold=True)
    setup(
# @added 20260211 - Branch #5706: v0.21.91
	name='tsfresh',
# @modified 20260602 - Branch #5750: v0.21.92
#	version='0.21.91',
	version='0.21.92',
    )
