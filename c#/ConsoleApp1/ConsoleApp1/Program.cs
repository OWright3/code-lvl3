using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        { 
            int age;
            int c = 0;
            string name;


            while (c != 1)
            {
                name = TakeInput(x1: "Name bitch:");
                switch (name)
                {
                    case "stop":
                        c = 1;
                        break;
                    default:
                        age = Convert.ToInt32(TakeInput(x1:"Age bitch:"));
                        Console.WriteLine((age < 18) ? "Fuck outta here with that underage shit" : "You're {0}, and {1} years old", name, age);
                        break;
                }
            }
            
            static string TakeInput(string x1)
            {
                Console.WriteLine(x1);
                x1 = Console.ReadLine();

                return x1;
            }

        }
    }
}