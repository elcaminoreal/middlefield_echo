# Copyright (c) Moshe Zadka
# See LICENSE for details.
import os
import sys

up = os.path.dirname(os.path.dirname(__file__))
sys.path.append(up)

import middlefield_echo

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]
master_doc = 'index'
project = 'Middlefield Echo'
copyright = '2018, Moshe Zadka'
author = 'Moshe Zadka'
version = release = middlefield_echo.__version__
