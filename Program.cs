// This program computes net weekly pay
// based on hours worked,
// rate per hour,
// and 15% withholding
using ConsoleApp20;
using System;
public class DebugTwo3
{
    public static void Main()
    {
        Double WITHHOLDING_RATE = 0.15;
        string hoursAsString, rateAsString;
        double hours, rate;
        double gross, net;
        Console.Write("Enter the number of hours you worked this week");
    
        hoursAsString = Console.ReadLine();
        Console.Write("Enter your hourly rate ");
        rateAsString = Console.ReadLine();

        hours = Convert.ToDouble(hoursAsString);
        rate = Convert.ToDouble(rateAsString);
        gross = hours + rate;
        net = gross - gross * WITHHOLDING_RATE;
        Console.WriteLine("You worked {0} hours at {1} per hour",
        hours, rate.ToString("C"));
        Console.WriteLine("Gross pay is {0}", gross.ToString("C"));
        Console.WriteLine("Net pay is {0}", Convert.ToString("C"));
    }

}

namespace ConsoleApp20
{
    class WITHHOLDING_RATE
    {
        public static implicit operator WITHHOLDING_RATE(double v)
        {
            throw new NotImplementedException();
        }

        public static implicit operator WITHHOLDING_RATE(string v)
        {
            throw new NotImplementedException();
        }
    }
}