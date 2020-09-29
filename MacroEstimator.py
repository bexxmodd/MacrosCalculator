class Person:
    """Person class creates an user object"""

    _weight = 0
    _height = 0
    _age = 0
    _gender = 'male'
    _body_fat = 0

    def __init__(self):
        return

    @property
    def weight(self) -> float:
        return self._weight
    
    @weight.setter
    def weight(self, weight: float):
        self._weight = weight

    @property
    def height(self) -> float:
        return self._weight

    @height.setter
    def height(self, height):
        self._height = height
    
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age
    
    @property
    def gender(self) -> str:
        return self._gender
    
    @gender.setter
    def gender(self, gender: str) -> None:
        self._gender = gender
    
    @property
    def body_fat(self) -> float:
        return self._body_fat

    @body_fat.setter
    def body_fat(self, body_fat: float):
        if body_fat:
            self._body_fat = body_fat
        else:
            self._body_fat = self._approximate_body_fat()

    @property
    def body_mass_index(self) -> float:
        """BMI is a measure of body fat based on height
        and weight that applies to adult men & women."""
        return round((self._weight / (self._height * 12) ** 2) * 7, 4)

    def approximate_body_fat(self) -> None:
        """Approximates body fat % based on given weight, height, age."""
        if self._gender == 'female':
            self._body_fat = (1.2 * self.body_mass_index * 100) + (0.23 * self._age) - 5.4
        elif self._gender == 'male':
            self._body_fat = (1.2 * self.body_mass_index * 100) + (0.23 * self._age) - 16.2


class Athlete(Person):
    """Inherits main measures from Person.
    Adds activity variables to the pack"""

    _exercise_freq = 'Occasionally'
    _active_job = False
    _goal = 'Lose Weight'

    @property
    def exercise_freq(self) -> str:
        return self._exercise_freq

    @exercise_freq.setter
    def exercise_freq(self, freq: str):
        self._exercise_freq = freq

    @property
    def active_job(self) -> str:
        return self._active_job

    @active_job.setter
    def active_job(self, job: str) -> None:
        self._active_job = job
    
    @property
    def goal(self) -> str:
        return self._goal

    @goal.setter
    def goal(self, goal: str):
        self._goal = goal

    
class Measurements():
    """Calculate body measurements and indices of a Person"""

    def __init__(self, person: Person=None):
        if person is None:
            self.person = Person()
        else:
            self.person = person

    def lean_body_mass(self) -> float:
        """LBM is a part of body composition that is defined
        as the difference between body weight and body fat weight."""
        return self.person.weight * (1 - self.person.body_fat / 100)

    def basal_metabolic_rate(self) -> float:
        """BMR is calories required to keep your body functioning at rest.
        
        BMR is also known as your body's metabolism; therefore, any increase
        to your metabolic weight, such as exercise, will increase your BMR.
        """
        if self.person.gender == 'male':
            return 66 + (6.23 * self.person.weight) + (12.7 * self.person.height * 12) - (6.8 * self.person.age)
        elif self.person.gender == 'female':
            return 665 + (4.35 * self.person.weight) + (4.7 * self.person.height * 12) - (4.7 * self.person.age)

    def protein_requirement(self) -> float:
        """Minimum protein amount (in grams) needed for your body weight"""
        return self.lean_body_mass() / 2.20462 * 2.25


class Diet():
    """Creates a dispersal of the macros based on a fitness goal.
    Uses Person class to approximate various indexed and diet type.
    """

    PROTEIN_KCAL = 4
    CARBS_KCAL = 4
    FATS_KCAL = 9

    def __init__(self,
                athlete: Athlete = None) -> None:
        if athlete is None:
            self.athlete = Athlete()
        else:
            self.athlete = athlete

        # Initially macro variables are set to zero
        self.protein = 0
        self.carbs = 0
        self.fats = 0
        self.total = 0
        
    @property
    def set_protein(self):
        return self.protein

    @set_protein.setter
    def set_protein(self, protein: float) -> None:
        self.protein = protein

    @property
    def set_carbs(self):
        return self.carbs

    @set_carbs.setter
    def set_carbs(self, carbs: float) -> None:
        self.carbs = carbs

    @property
    def set_fats(self) -> float:
        return self.fats

    @set_fats.setter
    def set_fats(self, fats: float) -> None:
        self.fats = fats

    @property
    def set_total(self) -> float:
        return self.total

    @set_total.setter
    def set_total(self, total: float) -> None:
        self.total = total

    def set_macros(self, goal: str, weight: float) -> None:
        """Asign diet macro values based on a goal"""
        if goal == 'Gain Weight':
            self.protein = weight * self.PROTEIN_KCAL
            self.carbs = weight * 2 * self.CARBS_KCAL
            self.fats = weight * 0.45 * self.FATS_KCAL

        elif goal == 'Lose Weight':
            self.protein = weight * 1.4 * self.PROTEIN_KCAL
            self.carbs = weight * self.CARBS_KCAL
            self.fats = weight * 0.25 * self.FATS_KCAL

        elif goal == 'Maintain Weight':
            self.protein = weight * self.PROTEIN_KCAL
            self.carbs = weight * 1.6 * self.CARBS_KCAL
            self.fats = weight * 0.35 * self.FATS_KCAL

        self.total = sum([self.protein, self.carbs, self.fats])

    def total_daily_energy_expenditure(self) -> float:
        """TDEE is an estimation of calories burned per day,
        when exercise and job activity is taken into account.
        ...
        :return: BMR adjusted for the exercise amount.
        :rtype: int
        """
        m = Measurements(self.athlete)
        tdee = 0

        if self.athlete.exercise_freq == 'Occasionally':
            tdee = m.basal_metabolic_rate() * 1.2
        elif self.athlete.exercise_freq == '1 to 2 Day':
            tdee = m.basal_metabolic_rate() * 1.375
        elif self.athlete.exercise_freq == '3 to 4 days':
            tdee = m.basal_metabolic_rate() * 1.55
        elif self.athlete.exercise_freq == '5 to 7 days':
            tdee = m.basal_metabolic_rate() * 1.725

        # Additional multiplier if the user has a physically active job.
        if self.athlete.active_job == True:
            return tdee * 1.15
        return tdee

    def calculate_macros_gain(self) -> dict:
        """Calculates macros (Proteins, Carbs, Fats) for the muscle gain.
        ...
        :return: protein, carbs, fats, totals: Returns macros as Kcal.
        :rtype: dict
        """
        if self.goal == 'Gain Weight':
            tdee = self.total_daily_energy_expenditure()
            if tdee > self.total:
                diff = tdee - self.total
                while self.total <= tdee + 500:
                    self.protein += diff * (self.protein / self.total)
                    self.carbs += diff * (self.carbs / self.total)
                    self.fats += diff * (self.fats / self.total)
                    self.total = sum([self.protein, self.carbs, self.fats])
            diet = {
                'protein': self.protein,
                'carbs': self.carbs,
                'fats': self.fats,
                'total': self.total
            }
            return diet
        else:
            raise TypeError(
                "This method is only for users who want to gain weight"
            )

    def calculate_macros_lose(self) -> dict:
        """
        Calculates macros (Proteins, Carbs, Fats) for the weight lose.
        """
        if self.goal == 'Lose Weight':
            tdee = self.total_daily_energy_expenditure()
            if tdee - self.total < 350:
                diff = 350 - (tdee - self.total)
                while self.total >= tdee - 350:
                    self.protein -= diff * (self.protein / self.total)
                    self.carbs -= diff * (self.carbs / self.total)
                    self.fats -= diff * (self.fats / self.total)
                    self.total = sum([self.protein, self.carbs, self.fats])
            diet = {
                'protein': self.protein,
                'carbs': self.carbs,
                'fats': self.fats,
                'total': self.total
            }
            return diet
        else:
            raise TypeError(
                "This method is only for users who want to lose weight"
            )

    def calculate_macros_maintain(self) -> dict:
        """Calculates macros (Proteins, Carbs, Fats) to maintain weight.
        ...
        :return: protein, carbs, fats, totals: Returns macros as Kcal.
        :rtype: dict
        """
        if self.goal == 'Maintain Weight':
            tdee = self.total_daily_energy_expenditure()
            if tdee > self.total:
                diff = tdee - self.total
                while self.total < tdee:
                    self.protein += 1
                    self.carbs += 1.6
                    self.fats += 0.35
                    self.total = sum([self.protein, self.carbs, self.fats])
            elif tdee < self.total:
                diff = self.total - tdee
                while self.total > tdee:
                    self.protein -= 1
                    self.carbs -= 1.6
                    self.fats -= 0.35
                    self.total = sum([self.protein, self.carbs, self.fats])
            diet = {
                'protein': self.protein,
                'carbs': self.carbs,
                'fats': self.fats,
                'total': self.total
            }
            return diet
        else:
            raise TypeError(
                "This method is only for users who want to maintain weight"
            )

    def __str__(self) -> str:
        return f'Protein: \t{round(self.protein / self.PROTEIN_KCAL, 1)} g. \t{int(self.protein)} kcal.\
            \nCarbs: \t{round(self.carbs / self.CARBS_KCAL, 1)} g. \t{int(self.carbs)} kcal.\
            \nFats: \t{round(self.fats /self.FATS_KCAL, 1)} g. \t{int(self.fats)} kcal.\
            \nTotal: \t\t{int(self.total)} kcal.'


if __name__ == '__main__':
    a = Diet()
    a.athlete.height=6.0
    a.athlete.weight=175
    a.athlete.age=30
    a.athlete.gender='male'
    a.athlete.approximate_body_fat()
    a.athlete.goal = 'Gain Weight'
    a.set_macros(a.athlete.goal, a.athlete.weight)
    print(a.total)