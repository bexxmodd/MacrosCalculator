import unittest
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
from MacroEstimator import Person


class TestPerson(unittest.TestCase):
    """Test Person class instantiation and and its methods"""
    
    @classmethod
    def setUpClass(cls):
        cls.male1 = Person(180, 6, 31, 'male')

    def test_person_object(self):
        self.assertIsInstance(self.male1, Person)

    def test_person_instantiation(self):
        self.assertEqual(self.male1.weight, 180)
        self.assertEqual(self.male1.height, 6)
        self.assertEqual(self.male1.age, 31)
        self.assertEqual(self.male1.gender, 'male')

    def test_without_bodyfat_instantiation(self):
        self.male1.set_body_fat()
        self.assertEqual(round(self.male1.body_fat, 1), 20.1)
    
    def test_raise_errors(self):
        with self.assertRaises(ValueError):
            person1 = (Person(-115, 5.4, 27, 'male', 19))
        with self.assertRaises(ValueError):
            person1 = (Person(115, -5.4, 27, 'male', 19))
        with self.assertRaises(ValueError):
            person1 = (Person(115, 5.4, -27, 'male', 19))

    def test_lean_body_mass(self):
        msg = ">> LBM is incorrectly calcualted <<"
        self.male1.set_body_fat()
        self.assertEqual(round(self.male1.lean_body_mass(), 1), 143.8, msg)

    def test_basal_metabolic_rate(self):
        male2 = Person(210, 6.5, 25, 'male', 8)
        female2 = Person(120, 5.2, 40, 'female', 22)
        msg = ">> BMR is incorrectly calculated <<"

        self.assertEqual(male2.basal_metabolic_rate(), 2194.9, msg)
        self.assertEqual(female2.basal_metabolic_rate(), 1292.28, msg)

    def test_protein_requirement(self):
        male3 = Person(230, 5.10, 23, 'male', 24)
        female3 = Person(135, 5.6, 34, 'female', 18)
        msg = '>> minimum protein requirement should is incorrectly calcualted <<'
        self.assertEqual(round(male3.protein_requirement(), 4),
                        178.3981, msg)
        self.assertEqual(round(female3.protein_requirement(), 4),
                        112.9787, msg)

if __name__ == '__main__':
    unittest.main()