import unittest
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
from MacroEstimator import Person
from MacroEstimator import Diet


class TestPerson(unittest.TestCase):
    """Test Diet class"""

    @classmethod
    def setUpClass(cls):
        person1 = Person(220, 7.1, 29, 'Male', 18)
        person2 = Person(132, 5.2, 37, 'feMale', 20)
        person3 = Person(120, 5.2, 40, 'female', 22)
        cls.diet1 = Diet(person1, '3 to 4 days', True, 'gain')
        cls.diet2 = Diet(person2, '1 to 2 Day', False, 'Lose')
        cls.diet3 = Diet(person1, 'Occasionally', True, 'maIntain')
        cls.diet4 = Diet(person2, '5 to 7 days', True, 'gain')
        cls.diet5 = Diet(person3, '3 to 4 days', False, 'maintain')

    def test_diet_instantiation(self):
        self.assertIsInstance(self.diet1, Diet)
        self.assertTrue(self.diet1.active_job)

    def test_macro_variables(self):
        for diet in [self.diet1, self.diet2, self.diet3]:
            diet.set_macros()

        self.assertEqual(self.diet1.protein, 880)
        self.assertEqual(self.diet1.carbs, 1760)
        self.assertEqual(self.diet1.fats, 891)
        self.assertEqual(self.diet1.total, 3531)

        self.assertAlmostEqual(self.diet2.protein, 739, 0)
        self.assertEqual(self.diet2.carbs, 528)
        self.assertEqual(self.diet2.fats, 297)
        self.assertAlmostEqual(self.diet2.total, 1564, 0)
        
        self.assertEqual(self.diet3.protein, 880)
        self.assertAlmostEqual(self.diet3.carbs, 1408, 1)
        self.assertAlmostEqual(self.diet3.fats, 695, -1)
        self.assertAlmostEqual(self.diet3.total, 2980, -1)

    def test_total_daily_energy_expenditure(self):
        self.assertAlmostEqual(
            self.diet4.total_daily_energy_expenditure(), 2695.08, 2)
        self.assertAlmostEqual(
            self.diet5.total_daily_energy_expenditure(), 2003.03, 2)

    def test_calculate_macros_gain(self):
        self.diet1.set_macros()
        macros_to_compare = {
            'protein': 1183,
            'carbs': 2365,
            'fats': 1200,
            'total': 4744
        }
        protein = self.diet1.calculate_macros_gain()['protein']
        carbs = self.diet1.calculate_macros_gain()['carbs']
        fats = self.diet1.calculate_macros_gain()['fats']
        total = self.diet1.calculate_macros_gain()['total']
        self.assertAlmostEqual(macros_to_compare['protein'], protein, -2)
        self.assertAlmostEqual(macros_to_compare['carbs'], carbs, -2)
        self.assertAlmostEqual(macros_to_compare['fats'], fats, -2)
        self.assertAlmostEqual(macros_to_compare['total'], total, -2)
        tdee = self.diet1.total_daily_energy_expenditure() + 600
        self.assertAlmostEqual(macros_to_compare['total'], tdee, -2)

    def test_method_raise_error(self):
        self.diet2.set_macros()
        with self.assertRaises(TypeError):
            self.diet2.calculate_macros_gain()

    def test_calculate_macros_lose(self):
        self.diet2.set_macros()
        macros_to_compare = {
            'protein': 700,
            'carbs': 500,
            'fats': 280,
            'total': 1480
        }
        protein = self.diet2.calculate_macros_lose()['protein']
        carbs = self.diet2.calculate_macros_lose()['carbs']
        fats = self.diet2.calculate_macros_lose()['fats']
        total = self.diet2.calculate_macros_lose()['total']
        self.assertAlmostEqual(macros_to_compare['protein'], protein, -2)
        self.assertAlmostEqual(macros_to_compare['carbs'], carbs, -2)
        self.assertAlmostEqual(macros_to_compare['fats'], fats, -2)
        self.assertAlmostEqual(macros_to_compare['total'], total, -2)
        tdee = self.diet2.total_daily_energy_expenditure() - 350
        self.assertAlmostEqual(macros_to_compare['total'], tdee, -2)

    def test_calculate_macros_maintain(self):
        self.diet3.set_macros()
        macros_to_compare = {
            'protein': 1000,
            'carbs': 1500,
            'fats': 720,
            'total': 3200
        }
        protein = self.diet3.calculate_macros_maintain()['protein']
        carbs = self.diet3.calculate_macros_maintain()['carbs']
        fats = self.diet3.calculate_macros_maintain()['fats']
        total = self.diet3.calculate_macros_maintain()['total']
        self.assertAlmostEqual(macros_to_compare['protein'], protein, -2)
        self.assertAlmostEqual(macros_to_compare['carbs'], carbs, -2)
        self.assertAlmostEqual(macros_to_compare['fats'], fats, -2)
        self.assertAlmostEqual(macros_to_compare['total'], total, -2)
        tdee = self.diet3.total_daily_energy_expenditure()
        self.assertAlmostEqual(macros_to_compare['total'], tdee, -2)

    @unittest.skip('Cannot decide how to check print')
    def test_print_macros(self):
        self.diet4.set_macros()
        self.diet4.calculate_macros_gain()

    def test_goal_setter(self):
        self.diet5.set_macros()
        self.assertEqual(self.diet5.protein, 480)
        self.assertEqual(self.diet5.carbs, 768)
        self.assertEqual(self.diet5.fats, 378)
        self.assertEqual(self.diet5.total, 1626)
        
        # Check if macros change when goal changes
        self.diet5.set_goal('lose')
        self.assertEqual(self.diet5.goal, 'lose')
        self.assertEqual(self.diet5.protein, 672)
        self.assertEqual(self.diet5.carbs, 480)
        self.assertEqual(self.diet5.fats, 270)
        self.assertEqual(self.diet5.total, 1422)

if __name__ == '__main__':
    unittest.main()