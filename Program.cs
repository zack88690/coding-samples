using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] array1 = new int[] { 1, 2, 3, 4 };
            Console.WriteLine("There is a list!");
            Console.WriteLine();
            Console.WriteLine("Would you like to see in reverse order, sequential, view a specific position or quit? ");
            string input =
                Console.ReadLine();
            if (input.Contains("seq"))
            {
                for (int i = 0; i <= 3; i++)
                    Console.WriteLine(array1[i]);
                Console.ReadKey();

            }
            if (input.Contains("quit"))
            {
                System.Environment.Exit(1);

            }
            if (input.Contains("rev"))
            {
                for(int i = 3; i > -1; i--)
              
                    Console.WriteLine(array1[i]);
                Console.ReadKey();


            }
            if (input.Contains("spec"))
            {
                Console.WriteLine();
                Console.WriteLine();
                Console.WriteLine("Enter a specific point in the array, 0-MAX");
                Console.WriteLine("__________________________________________");
                string input2 =
                    Console.ReadLine();
                int inputto = Convert.ToInt32(input2);
                input2 = "";
                Console.WriteLine("__________________________________________");
                Console.WriteLine(array1[inputto]);
                Console.ReadKey();
            }
            if (input.Contains("add"))
            {
                Console.WriteLine();
                Console.WriteLine();
                Console.WriteLine("Enter what you'd like to add, keep in mind this list is an integer list.");
                string newadd =
                    Console.ReadLine();
                int newint = Convert.ToInt32(newadd);
                var tmplist = array1.ToList();
                tmplist.Add(newint);
                
                Console.WriteLine("Adding...");
                Console.WriteLine("Compiling...");
                Console.WriteLine("_____________");
                Console.WriteLine(tmplist);
            }
            Console.ReadKey();




        }
    }
}
