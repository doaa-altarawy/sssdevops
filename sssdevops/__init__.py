"""
Main init file for the sssdevop package
"""

from sssdevops import *
from .list_tools import mean
from .more_list_tools import split

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
