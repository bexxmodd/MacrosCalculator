""" -[] add line to calories function to make sure it works as inteded"""

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
        if self.gender.lower() == 'man' or self.gender.lower() == 'male':
            return 66 + (6.23 * self.weight) + (12.7 * self.height * 12) - (6.8 * self.age)
        if self.gender.lower() == 'woman' or self.gender.lower() == 'female':
            return 665 + (4.35 * self.weight) + (4.7 * self.height * 12) - (4.7 * self.age)

    def total_daily_energy_expenditure(self, exercise_days_number):
        """
        TDEE is an estimation of how calories burned per day when exercise is taken into account.

        :param exercise_days_number: Number of days you exercise per week.
        :type exercise_days_number: int
        ...
        :return: BMR adjusted for the exercise amount.
        :rtype: int
        """
        if exercise_days_number < 0:
            raise ValueError ('You can\'t have negative number days')
        elif exercise_days_number > 7:
            raise ValueError ('There are only 7 days in a week')
        if exercise_days_number < 1:
            return self._basal_metabolic_rate() * 1.2
        elif exercise_days_number >= 1 and exercise_days_number < 3:
            return self._basal_metabolic_rate() * 1.375
        elif exercise_days_number >= 3 and exercise_days_number < 5:
            return self._basal_metabolic_rate() * 1.55
        else:
            return self._basal_metabolic_rate() * 1.725

    def protein_requirement(self):
        """Minimum protein amount (in grams) needed for your body weight"""
        return self.lean_body_mass() / 2.20462 * 2.25