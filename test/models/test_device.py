"""Test experiment models"""
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies


class DeviceModels(unittest.TestCase):
    