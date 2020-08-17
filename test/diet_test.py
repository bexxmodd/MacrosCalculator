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
        cls.diet1 = Diet(
            '3 to 4 days', True, 'gain', 220, 7.1, 29, 'Male', 18
        )
        cls.diet2 = Diet(
            '1 to 2 Day', False, 'Lose', 132, 5.2, 37, 'feMale', 20
        )
        cls.diet3 = Diet(
            'Occasionally', True, 'maIntain', 155.5, 5.4, 25, 'female', 23.2
        )

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
        
        self.assertEqual(self.diet3.protein, 622)
        self.assertAlmostEqual(self.diet3.carbs, 995.2, 1)
        self.assertAlmostEqual(self.diet3.fats, 489.8, 1)
        self.assertAlmostEqual(self.diet3.total, 2107, 0)

    def test_total_daily_energy_expenditure(self):
        diet4 = Diet(
            '5 to 7 days', True, 'gain', 210, 6.5, 25, 'Male', 8
        )
        diet5 = Diet(
            '3 to 4 days', False, 'maintain', 120, 5.2, 40, 'female', 22
        )
        diet6 = Diet(
            'Occasionally', True, 'maintain', 120, 5.2, 40, 'female', 22
        )
        self.assertAlmostEqual(diet4.total_daily_energy_expenditure(), 4354.13, 2)
        self.assertAlmostEqual(diet5.total_daily_energy_expenditure(), 2003.03, 2)
        self.assertAlmostEqual(diet6.total_daily_energy_expenditure(), 1783.35, 2)

    def test_calculate_macros_gain(self):
        diet7 = Diet(
            '3 to 4 days', False, 'gain', 120, 5, 30, 'female', 22
        )
        diet7.set_macros()
        macros_to_compare = {
            'protein': 640,
            'carbs': 1300,
            'fats': 650,
            'total': 2586
        }
        protein = diet7.calculate_macros_gain()['protein']
        carbs = diet7.calculate_macros_gain()['carbs']
        fats = diet7.calculate_macros_gain()['fats']
        total = diet7.calculate_macros_gain()['total']
        self.assertAlmostEqual(macros_to_compare['protein'], protein, -2)
        self.assertAlmostEqual(macros_to_compare['carbs'], carbs, -2)
        self.assertAlmostEqual(macros_to_compare['fats'], fats, -2)
        self.assertAlmostEqual(macros_to_compare['total'], total, -2)
        tdee = diet7.total_daily_energy_expenditure() + 500
        self.assertAlmostEqual(macros_to_compare['total'], tdee, -2)

    def test_method_raise_error(self):
        diet_error = Diet(
            '3 to 4 days', False, 'lose', 120, 5, 30, 'female', 22
        )
        diet_error.set_macros()
        with self.assertRaises(TypeError):
            diet_error.calculate_macros_gain()

    def test_calculate_macros_lose(self):
        diet8 = Diet(
            '3 to 4 days', True, 'lose', 230, 5.9, 36, 'female', 32
        )
        diet8.set_macros()
        macros_to_compare = {
            'protein': 1300,
            'carbs': 900,
            'fats': 500,
            'total': 2700
        }
        protein = diet8.calculate_macros_lose()['protein']
        carbs = diet8.calculate_macros_lose()['carbs']
        fats = diet8.calculate_macros_lose()['fats']
        total = diet8.calculate_macros_lose()['total']
        self.assertAlmostEqual(macros_to_compare['protein'], protein, -2)
        self.assertAlmostEqual(macros_to_compare['carbs'], carbs, -2)
        self.assertAlmostEqual(macros_to_compare['fats'], fats, -2)
        self.assertAlmostEqual(macros_to_compare['total'], total, -2)
        tdee = diet8.total_daily_energy_expenditure() - 550
        self.assertAlmostEqual(macros_to_compare['total'], tdee, -2)

    def test_calculate_macros_maintain(self):
        diet9 = Diet(
            'Occasionally', True, 'maintain', 185, 5.11, 32, 'male', 17.5
        )
        diet9.set_macros()
        macros_to_compare = {
            'protein': 700,
            'carbs': 1200,
            'fats': 550,
            'total': 2500
        }
        protein = diet9.calculate_macros_maintain()['protein']
        carbs = diet9.calculate_macros_maintain()['carbs']
        fats = diet9.calculate_macros_maintain()['fats']
        total = diet9.calculate_macros_maintain()['total']
        self.assertAlmostEqual(macros_to_compare['protein'], protein, -2)
        self.assertAlmostEqual(macros_to_compare['carbs'], carbs, -2)
        self.assertAlmostEqual(macros_to_compare['fats'], fats, -2)
        self.assertAlmostEqual(macros_to_compare['total'], total, -2)
        tdee = diet9.total_daily_energy_expenditure()
        self.assertAlmostEqual(macros_to_compare['total'], tdee, -2)


    def test_print_macros(self):
        diet10 = Diet(
            'Occasionally', True, 'gain', 165, 6.6, 22, 'male', 11
        )
        diet10.set_macros()
        diet10.calculate_macros_gain()

    def test_goal_setter(self):
        diet11 = Diet(
            'Occasionally', False, 'gain', 155, 6.2, 25, 'male', 15
        )
        diet11.set_macros()
        self.assertEqual(diet11.protein, 620)
        self.assertEqual(diet11.carbs, 1240)
        self.assertEqual(diet11.fats, 627.75)
        self.assertEqual(diet11.total, 2487.75)
        
        # Check if macros change when goal changes
        diet11.set_goal('lose')
        self.assertEqual(diet11.goal, 'lose')
        self.assertEqual(diet11.protein, 868)
        self.assertEqual(diet11.carbs, 620)
        self.assertEqual(diet11.fats, 348.75)
        self.assertEqual(diet11.total, 1836.75)

if __name__ == '__main__':
    unittest.main()