import unittest
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
from MacroEstimator import Person, Diet
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt

class TestUi(unittest.TestCase):
    """Test UI class"""

    def test_defaults(self):
        """Test the GUI in its default state"""
        pass



if __name__ == '__main__':
    unittest.main()