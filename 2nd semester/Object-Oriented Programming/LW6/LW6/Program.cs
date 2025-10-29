using LW6;
class Program
{
    static void Main()
    {
        Console.Write("Enter the starting number of the range: ");
        int start = int.Parse(Console.ReadLine());

        Console.Write("Enter the ending number of the range: ");
        int finish = int.Parse(Console.ReadLine());

        int rangeSize = finish - start + 1;
        int[] numbers = new int[rangeSize];
        int[] maximumValues = new int[rangeSize];
        int[] iterationCounts = new int[rangeSize];

        for (int i = 0; i < rangeSize; i++)
        {
            int currentNumber = start + i;

            FunctionCalculator calculator = new FunctionCalculator(currentNumber);
            calculator.CalculateFunction();

            numbers[i] = currentNumber;
            maximumValues[i] = calculator.GetMaxValue();
            iterationCounts[i] = calculator.GetIterationsCount();
        }


        int smallestIterationsIndex = 0;
        int largestIterationsIndex = 0;

        for (int i = 1; i < rangeSize; i++)
        {
            if (iterationCounts[i] < iterationCounts[smallestIterationsIndex])
                smallestIterationsIndex = i;

            if (iterationCounts[i] > iterationCounts[largestIterationsIndex])
                largestIterationsIndex = i;
        }



        Console.WriteLine("\nNumber with the smallest amount of iterations:\nNumber\tMaximum\tIterations");
        Console.WriteLine($"{numbers[smallestIterationsIndex]}\t{maximumValues[smallestIterationsIndex]}\t{iterationCounts[smallestIterationsIndex]}");

        Console.WriteLine("\nNumber with the largest amount of iterations:\nNumber\tMaximum\tIterations");
        Console.WriteLine($"{numbers[largestIterationsIndex]}\t{maximumValues[largestIterationsIndex]}\t{iterationCounts[largestIterationsIndex]}");
    }
}
