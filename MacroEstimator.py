

class Person:
    """Person class creates an user object and computes its lean body mass
    basal metabolic rate and protein requirement to maintain same weight.
    
    :param weight: body weight in pounds.
    :type weight: int
    :param height: height in feet.
    :type height: int
    :param body_fat: user's body fat as percentage,
        e.i. if body fat is 15% of total weight enter 15.
    :type body_fat: float, optional
    :param age: user's age in years.
    :type age: int
    :param gender: gender of the user.
    :type gender: string
    """

    def __init__(self, weight, height, body_fat=17, age, gender):
        self.weight = weight
        self.height = height
        self.body_fat = body_fat
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'Weight: {self.weight} lbs\n' \
            + f'Height: {self.height}'

    @classmethod
    def set_body_fat(self):
        self.body_fat = approximate_body_fat()

    def lean_body_mass(self):
        """
        Lean body mass (LBM) is a part of body composition that is defined
        as the difference between total body weight and body fat weight.
        """
        return self.weight * (1 - (self.body_fat / 100))

    def basal_metabolic_rate(self):
        """BMR is the number of calories required to keep your body functioning at rest.
        
        BMR is also known as your body's metabolism; therefore, any increase
        to your metabolic weight, such as exercise, will increase your BMR.
        """
        if self.gender.lower() == 'male':
            return 66 + (6.23 * self.weight) + (12.7 * self.height * 12) - (6.8 * self.age)
        elif self.gender.lower() == 'female':
            return 665 + (4.35 * self.weight) + (4.7 * self.height * 12) - (4.7 * self.age)

    def protein_requirement(self):
        """Minimum protein amount (in grams) needed for your body weight"""
        return self.lean_body_mass() / 2.20462 * 2.25


class Diet():
        
    PROTEIN_KCAL = 4
    CARBS_KCAL = 4
    FATS_KCAL = 9

    def __init__(self, exercise_frequency, active_job=False, goal, *args):
        weight, height, body_fat, age, gender = args
        self.person = Person(weight, height, body_fat, age, gender)
        self.exercise_frequency = exercise_frequency
        self.active_job = active_job
        self.goal = goal.lower()
        if goal == 'gain':
            self.protein = person.weight * self.PROTEIN_KCAL
            self.carbs = person.weight * 2 * self.CARBS_KCAL
            self.fats = person.weight * 0.45 * self.FATS_KCAL
        elif goal = 'lose':
            self.protein = person.weight * 1.4 * self.PROTEIN_KCAL
            self.carbs = person.weight * self.CARBS_KCAL
            self.fats = person.weight * 0.25 * self.FATS_KCAL
        elif goal = 'maintain':
            self.protein = person.weight * self.PROTEIN_KCAL
            self.carbs = person.weight * 1.6 * self.CARBS_KCAL
            self.fats = person.weight * 0.35 * self.FATS_KCAL
        self.total = sum([self.protein, self.carbs, self.fats])

    def total_daily_energy_expenditure(self):
        """
        TDEE is an estimation of how calories burned per day
        when exercise and job activity is taken into account.
        ...
        :return: BMR adjusted for the exercise amount.
        :rtype: int
        """
        tdee = 0
        if self.exercise_frequency == 'Occasionally':
            tdee = self.person.basal_metabolic_rate() * 1.2
        elif self.exercise_frequency == '1 to 2 Day':
            tdee = self.person.basal_metabolic_rate() * 1.375
        elif self.exercise_frequency == '3 to 4 days':
            tdee = self.person.basal_metabolic_rate() * 1.55
        elif self.exercise_frequency == '5 to 7 days':
            tdee = self.person.basal_metabolic_rate() * 1.725
        # Additional multiplier if the user has a physically active job.
        if self.active_job == True:
            return tdee * 1.15
        elif self.active_job == False:
            return tdee

    def calculate_macros_gain(self):
        """Calculates macros (Proteins, Carbs, Fats) for the muscle gain.
        ...
        :return: protein, carbs, fats, totals: Returns macros as Kcal.
        :rtype: dict
        """
        tdee = self.total_daily_energy_expenditure()
        if tdee > self.total:
            diff = tdee - self.total
            while self.total <= tdee + 500:
                self.protein += diff * (self.protein / self.total)
                self.carbs += diff * (self.carbs / self.total)
                self.fats += diff * (self.fats / self.total)
                self.total = sum([self.protein, self.carbs, self.fats])
        diet = {
            'protein': protein,
            'carbs': carbs,
            'fats': fats,
            'self.total kcals': sum([protein, carbs, fats])
        }
        return diet

    def calculate_macro_lose(self):
        """Calculates macros (Proteins, Carbs, Fats) for the weight lose.
        ...
        :return: protein, carbs, fats, totals: Returns macros as Kcal.
        :rtype: dict
        """
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
            'total kcals': self.total
        }
        return diet

    def calculate_macro_maintain():
        """Calculates macros (Proteins, Carbs, Fats) to maintain weight.
        ...
        :return: protein, carbs, fats, totals: Returns macros as Kcal.
        :rtype: dict
        """
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
                self.protein += 1
                self.carbs += 1.6
                self.fats += 0.35
                self.total = sum([self.protein, self.carbs, self.fats])
        dier = {
            'protein': protein,
            'carbs': carbs,
            'fats': fats,
            'total kcals': self.total
        }
        return diet

    def __str__ (self):
        """Prints the chosen diet with macros as grams & kcal, and totals as kcal."""
        if self.goal == 'gain':
            results = self.calculate_macros_gain()
        elif self.goal == 'lose':
            results = self.calculate_macro_lose()
        elif self.goal == 'maintain':
            results = self.calculate_macro_maintain()

        return f'Protein: \t{round(results["protein"] / self.PROTEIN_KCAL, 1)} g. \t{int(results["protein"])} kcal.\
            \nCarbs: \t{round(results["carbs"]/self.CARBS_KCAL, 1)} g. \t{int(results["carbs"])} kcal.\
            \nFats: \t{round(results["fats"]/self.FATS_KCAL, 1)} g. \t{int(results["fats"])} kcal.\
            \nTotal: \t\t{int(results["total"])} kcal.'
