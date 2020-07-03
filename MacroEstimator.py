

class macroCaloriesEstimator:
    """The class calculates various body indexes like LBM, BMR & TDEE.
    Also computes macros as the share of the total daily kcals.
    
    :param weight: body weight in pounds
    :type weight: int
    :param height: height in feet
    :type height: int
    :param body_fat: user's body fat as percentage, e.i. if body fat is 15% of total weight enter 15
    :type body_fat: float, optional
    :param age: user's age in years
    :type age: int
    :param gender: gender of the user. Can take both args, "Male/Female" of "Man/Women"
    :type gender: string
    """
    
    PROTEIN_KCAL = 4
    CARBS_KCAL = 4
    FATS_KCAL = 9
    
    def __init__(self, weight, height, body_fat, age, gender):
        self.weight = weight
        self.height = height
        self.body_fat = body_fat
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'Weight: {self.weight} lbs\nBody fat: {self.body_fat} %\nHeight: {self.height}'

    def lean_body_mass(self):
        """
        Lean body mass (LBM) is a part of body composition that is defined
        as the difference between total body weight and body fat weight.
        """
        return self.weight * (1 - (self.body_fat / 100))

    def _basal_metabolic_rate(self):
        """BMR is the number of calories required to keep your body functioning at rest.
        
        BMR is also known as your body's metabolism; therefore,
        any increase to your metabolic weight, such as exercise, will increase your BMR.
        """
        if self.gender.lower() == 'male':
            return 66 + (6.23 * self.weight) + (12.7 * self.height * 12) - (6.8 * self.age)
        elif self.gender.lower() == 'female':
            return 665 + (4.35 * self.weight) + (4.7 * self.height * 12) - (4.7 * self.age)

    def total_daily_energy_expenditure(self, exercise_frequency, active_job):
        """
        TDEE is an estimation of how calories burned per day when exercise is taken into account.

        :param exercise_frequency: Number of days you exercise per week.
        :type exercise_frequency: int
        ...
        :return: BMR adjusted for the exercise amount.
        :rtype: int
        """
        tdee = 0
        if exercise_frequency == 'Occasionally':
            tdee = self._basal_metabolic_rate() * 1.2
        elif exercise_frequency == '1 to 2 Day':
            tdee = self._basal_metabolic_rate() * 1.375
        elif exercise_frequency == '3 to 4 days':
            tdee = self._basal_metabolic_rate() * 1.55
        elif exercise_frequency == '5 to 7 days':
            tdee = self._basal_metabolic_rate() * 1.725
        # Additional multiplier if the user has a physically active job.
        if active_job == 'Yes':
            return tdee * 1.15
        elif active_job == 'No':
            return tdee

    def protein_requirement(self):
        """Minimum protein amount (in grams) needed for your body weight"""
        return self.lean_body_mass() / 2.20462 * 2.25

    def diet_macros(self, diet_type, exercise_frequency, active_job):
        """Calculates macros (Proteins, Carbs, Fats) for a chosen diet.

        :param diet_type: Three options of diet 'gain', 'lose', 'maintain'
        :type diet_type: string
        ...
        :return: protein, carbs, fats, totals: Returns macros as Kcal.
        :rtype: int
        """
        if diet_type.lower() == 'gain':
            protein = self.weight * self.PROTEIN_KCAL
            carbs = self.weight * 2 * self.CARBS_KCAL
            fats = self.weight * 0.45 * self.FATS_KCAL
            total = sum([protein, carbs, fats])
            tdee = self.total_daily_energy_expenditure(exercise_frequency, active_job)
            if tdee > total:
                diff = tdee - total
                while total <= tdee + 500:
                    protein += diff * (protein/total)
                    carbs += diff * (carbs/total)
                    fats += diff * (fats/total)
                    total = sum([protein, carbs, fats])
            return protein, carbs, fats, sum([protein, carbs, fats])

        elif diet_type.lower() == 'lose':
            protein = self.weight * 1.4 * self.PROTEIN_KCAL
            carbs = self.weight * self.CARBS_KCAL
            fats = self.weight * 0.25 * self.FATS_KCAL
            total = sum([protein, carbs, fats])
            tdee = self.total_daily_energy_expenditure(exercise_frequency, active_job)
            if tdee - total < 350:
                diff = 350 - (tdee - total)
                while total >= tdee - 350:
                    protein -= diff * (protein/total)
                    carbs -= diff * (carbs/total)
                    fats -= diff * (fats/total)
                    total = sum([protein, carbs, fats])
            return protein, carbs, fats, sum([protein, carbs, fats])
            
        elif diet_type.lower()== 'maintain':
            protein = self.weight * self.PROTEIN_KCAL
            carbs = self.weight * 1.6 * self.CARBS_KCAL
            fats = self.weight * 0.35 * self.FATS_KCAL
            total = sum([protein, carbs, fats])
            tdee = self.total_daily_energy_expenditure(exercise_frequency, active_job)
            if tdee > total:
                diff = tdee - total
                while total < tdee:
                    protein += 1
                    carbs += 1.6
                    fats += 0.35
                    total = sum([protein, carbs, fats])
            elif tdee < total:
                diff = total - tdee
                while total > tdee:
                    protein += 1
                    carbs += 1.6
                    fats += 0.35
                    total = sum([protein, carbs, fats])
            return protein, carbs, fats, sum([protein, carbs, fats])

    def print_macros(self, diet_type, exercise_frequency, active_job):
        """Prints the chosen diet with macros as grams & kcal, and totals as kcal."""
        if diet_type.lower() == 'gain':
            protein, carbs, fats, total = self.diet_macros(diet_type, exercise_frequency, active_job)
        elif diet_type.lower() == 'lose':
            protein, carbs, fats, total = self.diet_macros(diet_type, exercise_frequency, active_job)
        elif diet_type.lower() == 'maintain':
            protein, carbs, fats, total = self.diet_macros(diet_type, exercise_frequency, active_job)
        return f'Protein: \t{round(protein/self.PROTEIN_KCAL, 1)} g. \t{int(protein)} kcal.\
            \nCarbs: \t{round(carbs/self.CARBS_KCAL, 1)} g. \t{int(carbs)} kcal.\
            \nFats: \t{round(fats/self.FATS_KCAL, 1)} g. \t{int(fats)} kcal.\
            \nTotal: \t\t{int(total)} kcal.'
