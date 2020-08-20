import unittest
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
from MacroEstimator import Person
from MacroEstimator import Diet

class TestUi(unittest.TestCase):
    """Test UI class"""

    def test_input_values(self):
        pass



if __name__ == '__main__':
    unittest.main()