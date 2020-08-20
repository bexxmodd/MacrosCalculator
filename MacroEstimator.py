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

    def __init__(self, weight, height, age, gender, body_fat = None):
        if all(v > 0 for v in [weight, height, age]):
            self.weight = weight
            self.height = height
            self.age = age
        else:
            raise ValueError('Cannot take negative values!')
        self.gender = gender
        self.body_fat = body_fat

    def __str__(self):
        return f'Weight:{self.weight}lbs Height:{self.height}ft Age:{self.age} Gender:{self.gender}'
    
    def set_body_fat(self):
        self.approximate_body_fat()

    def approximate_body_fat(self):
        """Approximates body fat % based on given weight, height, age"""
        if self.gender == 'female':
            self.body_fat = (1.2 * self.body_mass_index() * 100) + (0.23 * self.age) - 5.4
        elif self.gender == 'male':
            self.body_fat = (1.2 * self.body_mass_index() * 100) + (0.23 * self.age) - 16.2

    def body_mass_index(self):
        """BMI is a measure of body fat based on height and weight that applies to adult men & women"""
        return round((self.weight / (self.height * 12) ** 2) * 7, 4)

    def lean_body_mass(self):
        """
        Lean body mass (LBM) is a part of body composition that is defined
        as the difference between total body weight and body fat weight.
        """
        return self.weight * (1 - self.body_fat / 100)

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
    """Creates a distribution of the macros in grams and kcal based on a goal
    class uses Person class to approximate various indexed and diet type.

    :param execise_frequency: how many days of exercise per week.
    :type execise_frequency: str
    :param active_job: If a person holds physically active job
    :type active_job: boolean
    :param goal: what person is trying to achieve with the diet
    :type goal: str
    :param person: takes a Person object
    :type person: Person
    """

    PROTEIN_KCAL = 4
    CARBS_KCAL = 4
    FATS_KCAL = 9

    def __init__(self, person, exercise_frequency, active_job, goal):
        self.person = person
        self.exercise_frequency = exercise_frequency
        self.active_job = active_job
        self.goal = goal
        # We initialy set macro variables equal to zero
        self.protein, self.carbs, self.fats, self.total = 0, 0, 0, 0

    def set_goal(self, goal):
        self.goal = goal.lower()
        self.set_macros()

    def set_macros(self):
        if self.goal == 'Gain Weight':
            self.protein = self.person.weight * self.PROTEIN_KCAL
            self.carbs = self.person.weight * 2 * self.CARBS_KCAL
            self.fats = self.person.weight * 0.45 * self.FATS_KCAL
        elif self.goal == 'Lose Weight':
            self.protein = self.person.weight * 1.4 * self.PROTEIN_KCAL
            self.carbs = self.person.weight * self.CARBS_KCAL
            self.fats = self.person.weight * 0.25 * self.FATS_KCAL
        elif self.goal == 'Maintain Weight':
            self.protein = self.person.weight * self.PROTEIN_KCAL
            self.carbs = self.person.weight * 1.6 * self.CARBS_KCAL
            self.fats = self.person.weight * 0.35 * self.FATS_KCAL
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
            raise TypeError("This method is only for users who want to gain weight")

    def calculate_macros_lose(self):
        """Calculates macros (Proteins, Carbs, Fats) for the weight lose.
        ...
        :return: protein, carbs, fats, totals: Returns macros as Kcal.
        :rtype: dict
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
            raise TypeError("This method is only for users who want to lose weight")

    def calculate_macros_maintain(self):
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
            raise TypeError("This method is only for users who want to maintain weight")

    def __str__(self):
        return f'Protein: \t{round(self.protein / self.PROTEIN_KCAL, 1)} g. \t{int(self.protein)} kcal.\
            \nCarbs: \t{round(self.carbs / self.CARBS_KCAL, 1)} g. \t{int(self.carbs)} kcal.\
            \nFats: \t{round(self.fats /self.FATS_KCAL, 1)} g. \t{int(self.fats)} kcal.\
            \nTotal: \t\t{int(self.total)} kcal.'

    def get_protein(self):
        return self.protein

    def get_carbs(self):
        return self.carbs

    def get_fats(self):
        return self.fats

    def get_total(self):
        return self.total
