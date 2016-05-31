#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: activate_toolbox.py
# Author: Christof Schöch

"""
__author__ = "CLiGS"
__authors__ = "Christof Schoech, Daniel Schloer"
__email__ = "christof.schoech@uni-wuerzburg.de"
__license__ = ""
__version__ = ""
__date__ = ""

# Script to add the "tmw" module to your syspath. 
# Run once with appropriate path to use "tmw" with "import".
"""

import sys
import os

# Enter the path to the folder in which your tmw folder is located.
sys.path.append(os.path.abspath("/home/christof/Repos/cligs/tmw/"))

# Optional: Activate to remove a (mistaken or redundant path)    
#sys.path.remove(os.path.abspath("/home/christof/Repos/cligs/tmw"))

# This is for checking whether the path settings are correct.
print(sys.path)
