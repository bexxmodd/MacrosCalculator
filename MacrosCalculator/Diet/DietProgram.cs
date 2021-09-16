using MacrosCalculator.User;

namespace MacrosCalculator.Diet
{
    /// <summary>
    /// Create a dispersal of the macros based on a fitness goal.
    /// Uses <c>Athlete</c> to approximate various indices and diet types
    /// </summary>
    public class DietProgram
    {
        public const int PROTEIN_KCAL = 4;
        public const int CARBS_KCAL = 4;
        public const int FATS_KCAL = 9;

        public Athlete athlete;
        public Macros macros;

        public DietProgram(Athlete _athlete, Macros _macros)
        {
            athlete = _athlete;
            macros = _macros;
        }

        /// <summary>
        /// Set up diet macros based on a <c>Athlete</c>'s <c>Goal</c>
        /// </summary>
        public void SetMacros()
        {
            switch (athlete.goal)
            {
                case Goal.Gain:
                    SetMacrosToGainWeight();
                    break;
                case Goal.Cut:
                    SetMacrosToCutWeight();
                    break;
                case Goal.Maintain:
                    SetMacrosToMaintainWeight();
                    break;
            }
        }

        private void SetMacrosToMaintainWeight()
        {
            macros.protein = athlete.weight * PROTEIN_KCAL;
            macros.carbs = athlete.weight * 1.6 * CARBS_KCAL;
            macros.fats = athlete.weight * 0.35 * FATS_KCAL;
        }

        private void SetMacrosToCutWeight()
        {
            macros.protein = athlete.weight * 1.4 * PROTEIN_KCAL;
            macros.carbs = athlete.weight * CARBS_KCAL;
            macros.fats = athlete.weight * 0.25 * FATS_KCAL;
        }

        private void SetMacrosToGainWeight()
        {
            macros.protein = athlete.weight * PROTEIN_KCAL;
            macros.carbs = athlete.weight * 2.0 * CARBS_KCAL;
            macros.fats = athlete.weight * 0.45 * FATS_KCAL;
        }

        /// <summary>
        /// TDEE is an estimation of calories burned per day,
        /// when exercise and job activity is taken into account.
        /// </summary>
        /// 
        /// <returns>
        /// BMR adjusted for the exercise amount as a <code>double</code>
        /// </returns>
        public double ComputeTotalDailyEnergyExpenditure()
        {
            var bmr = athlete.CalculateBasalMetabolicRate();
            if (athlete.activeJob)
                bmr *= 1.15;

            switch (athlete.exerciseFrequency)
            {
                case 0:
                case 1:
                    return bmr * 1.2;
                case 2:
                case 3:
                    return bmr * 1.375;
                case 4:
                case 5:
                    return bmr * 1.55;
                default:
                    return bmr * 1.725;
            }
        }

        /// <summary>
        /// Calculates <c>Macros</c> for the muscle gain diet program.
        /// </summary>
        public void SetMacrosForWeightGain()
        {
            var tdee = ComputeTotalDailyEnergyExpenditure();
            var totalKcal = macros.GetTotalKcal();
            if (tdee > totalKcal)
            {
                var diff = tdee - totalKcal;
                while (macros.GetTotalKcal() <= tdee + 500)
                {
                    macros.protein += diff * (macros.protein / totalKcal);
                    macros.carbs += diff * (macros.carbs / totalKcal);
                    macros.fats += diff * (macros.fats / totalKcal);
                }
            }
        }

        /// <summary>
        /// Calculates <c>Macros</c> for the weight loss diet program.
        /// </summary>
        public void SetMacrosForWeightCut()
        {
            var tdee = ComputeTotalDailyEnergyExpenditure();
            var totalKcal = macros.GetTotalKcal();
            if (tdee - totalKcal < 350)
            {
                var diff = 350 - (tdee - totalKcal);
                while (macros.GetTotalKcal() >= tdee - 350)
                {
                    macros.protein -= diff * (macros.protein / totalKcal);
                    macros.carbs -= diff * (macros.carbs / totalKcal);
                    macros.fats -= diff * (macros.fats / totalKcal);
                }
            }
        }

        /// <summary>
        /// Calculates <c>Macros</c> for the diet program to maintain weight.
        /// </summary>
        public void SetMacrosForWeightMaintain()
        {
            var tdee = ComputeTotalDailyEnergyExpenditure();
            if (tdee > macros.GetTotalKcal())
                while (macros.GetTotalKcal() < tdee)
                {
                    macros.protein += 1;
                    macros.carbs += 1.6;
                    macros.fats += 0.35;
                }
            else
                while (macros.GetTotalKcal() > tdee)
                {
                macros.protein -= 1;
                macros.carbs -= 1.6;
                macros.fats -= 0.35;
                }
        }
    }
}
