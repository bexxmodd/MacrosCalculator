import unittest
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
from MacroEstimator import Person


class TestPerson(unittest.TestCase):
    """Test Person class instantiation and and its methods"""

    def test_person_object(self):
        test_person = Person(330, 4.2, 29, 'male', 33)
        self.assertIsInstance(test_person, Person)

    def test_person_instantiation(self):
        male1 = Person(220, 7.1, 29, 'Male', 18)
        self.assertEqual(male1.weight, 220)
        self.assertEqual(male1.height, 7.1)
        self.assertEqual(male1.age, 29)
        self.assertEqual(male1.gender, 'male')
        self.assertEqual(male1.body_fat, 18)

    def test_without_bodyfat_instantiation(self):
        person0 = Person(180, 6, 31, 'Male')
        self.assertIsNone(person0.body_fat)
        person0.set_body_fat()
        self.assertEqual(round(person0.body_fat, 2), 20.10)
    
    def test_raise_errors(self):
        with self.assertRaises(ValueError):
            person1 = (Person(-115, 5.4, 27, 'male', 19))
        with self.assertRaises(ValueError):
            person1 = (Person(115, -5.4, 27, 'male', 19))
        with self.assertRaises(ValueError):
            person1 = (Person(115, 5.4, -27, 'male', 19))
        with self.assertRaises(TypeError):
            person1 = (Person(115, 5.4, 27, 'dog', 19))

    def test_lean_body_mass(self):
        female1 = Person(115, 5.5, 25, 'female', 22)
        msg = ">> LBM is incorrectly calcualted <<"
        self.assertEqual(female1.lean_body_mass(), 89.7, msg)

    def test_basal_metabolic_rate(self):
        male2 = Person(210, 6.5, 25, 'Male', 8)
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