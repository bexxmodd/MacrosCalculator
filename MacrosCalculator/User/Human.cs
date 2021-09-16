using System;

namespace MacrosCalculator.User
{
    /// <summary>
    /// Human class that has typical characteristics to measure
    /// various athlete indices and calculate required macro kcals
    /// to achieve desired goals
    /// </summary>
    public class Human : Measurements
    {
        // Weight is in pounds
        public double weight { get; set; }
        // Height is in feet
        public double height { get; set; }
        public double bodyFat { get; set; }
        public int age { get; set; }
        public Gender gender;

        public Human()
        {
            weight = 0.0;
            height = 0.0;
            bodyFat = 0.0;
            age = 0;
            gender = Gender.Female;
        }

        public Human(double _weight, double _height,
                    int _age, Gender _gender)
        {
            weight = _weight;
            height = _height;
            age = _age;
            gender = _gender;
            bodyFat = ApproximateBodyFat(height, weight);
        }

        public Human(double height, double weight,
                    int age, Gender gender,
                    double fat) : this(height, weight, age, gender)
        {
            bodyFat = fat;
        }

        public static double GetBodyMassIndex(double weight, double height)
        {
            return (weight / Math.Pow(height * 12, 2)) * 7;
        }

        public double ApproximateBodyFat(double height, double weight)
        {
            return gender == Gender.Male ?
                    ApproximateMaleBodyFat(height, weight) :
                    ApproximateFemaleBodyFat(height, weight);
        }

        private double ApproximateMaleBodyFat(double height, double weight)
        {
            var bmi = Human.GetBodyMassIndex(height, weight);
            return (1.2 * bmi * 100) + (0.23 * age) - 16.2;
        }

        private double ApproximateFemaleBodyFat(double height, double  weight)
        {
            var bmi = Human.GetBodyMassIndex(height, weight);
            return (1.2 * bmi * 100) + (0.23 * age) - 5.4;
        }

        public double CalculateLeanBodyMess()
        {
            return weight * (1 - bodyFat / 100);
        }

        public double CalculateBasalMetabolicRate()
        {
            return gender == Gender.Male ? 
                CalcMaleBasalMetabolicRate() : CalcFemaleBasalMetabolicRate();
        }

        private double CalcFemaleBasalMetabolicRate()
        {
            return 665 + (4.35 * weight) + (4.7 * height * 12) - (4.7 * age);
        }

        private double CalcMaleBasalMetabolicRate()
        {
            return 66 + (6.23 * weight) + (12.7 * height * 12) - (6.8 * age);
        }

    }

    public enum Gender : byte
    {
        Male = 0,
        Female = 1,
    }

}
