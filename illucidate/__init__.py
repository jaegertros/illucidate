"""
Illucidate: Early warning signals for bacterial detection.

A toolkit for discovering multivariate, time-structured patterns in
phage-based biosensor data that enable earlier pathogen detection.
"""

__version__ = "0.1.0"
__author__ = "Caleb Waddell"

# Make key classes easily accessible
from illucidate.adapters.base_adapter import BaseAdapter, quick_parse

__all__ = ['BaseAdapter', 'quick_parse', '__version__']
