"""
Main init file for the sssdevop package
"""

# from .sssdevops import *
from .list_tools import mean

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
