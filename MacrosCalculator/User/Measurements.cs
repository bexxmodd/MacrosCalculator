using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MacrosCalculator.User
{
    interface Measurements
    {
        public double CalculateLeanBodyMess();
        public double CalculateBasalMetabolicRate();

        public double CalculateProteinRequirement()
        {
            return CalculateLeanBodyMess() / 2.20462 * 2.25;
        }
    }
}
