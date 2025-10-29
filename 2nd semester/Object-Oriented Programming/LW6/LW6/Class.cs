namespace LW6
{
    class FunctionCalculator
    {
        private int number;
        private int iterations;
        private int maxValue;

        public FunctionCalculator(int number)
        {
            this.number = number;
            this.iterations = 0;
            this.maxValue = number;
        }

        public void CalculateFunction()
        {
            int value = number;

            while (value != 1)
            {
                value = (value % 2 == 0) ? value / 2 : value * 3 + 1;

                if (value > maxValue)
                    maxValue = value;

                iterations++;
            }
        }

        public int GetMaxValue()
        {
            return maxValue;
        }

        public int GetIterationsCount()
        {
            return iterations;
        }
    }
}
