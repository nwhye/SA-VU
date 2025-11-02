using System;

class Program
{
    static int[] SubtractSetByItself(int[] set)
    {
        int[] result = new int[set.Length];
        for (int i = 0; i < set.Length; i++)
        {
            result[i] = set[i] - set[i]; 
        }
        return result;
    }

    static void Main()
    {
        int[] setA = new int[] { 1 };
        int[] result = SubtractSetByItself(setA);
        Console.WriteLine("The result of set A subtrackted by set A is: " + string.Join(", ", result));
    }
}
