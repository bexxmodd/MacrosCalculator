
namespace MacrosCalculator.User
{
    /// <summary>
    /// Stores the data for the three main components of diet macros
    /// </summary>
    public struct Macros 
    {
        public double protein { get; set; }
        public double carbs { get; set; }
        public double fats { get; set; }

        /// <summary>
        /// Get the total count of the kcalories based on given macros
        /// </summary>
        /// 
        /// <returns>
        /// total kcal as <code>double</code>
        /// </returns>
        public double GetTotalKcal()
        {
            return protein + carbs + fats;
        }

        public override string ToString()
        {
            return $"Protein: {protein}, Carbs: {carbs}, Fats: {fats}";
        }
    }
}
