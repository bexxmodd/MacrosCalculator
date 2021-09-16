
namespace MacrosCalculator.User
{
    public class Athlete : Human
    {
        public int exerciseFrequency { get; set; }
        public bool activeJob { get; set; }
        public Goal goal { get; set; }

        public Athlete() : base()
        {
            exerciseFrequency = 0;
            activeJob = false;
            goal = Goal.Maintain;
        }
    }

    public enum Goal : byte
    {
        Maintain,
        Gain,
        Cut,
    }
}
