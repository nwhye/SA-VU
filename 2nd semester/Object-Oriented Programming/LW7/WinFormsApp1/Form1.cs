using System;

namespace WinFormsApp1
{
    public partial class Form1 : Form
    {

        public static string listBox_text = "";   ///bebebebebe

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            progressBar1.Visible = false;
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged_1(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)                           //button!!!
        {
            if (String.IsNullOrEmpty(textBox1.Text) || String.IsNullOrEmpty(textBox2.Text) || textBox1.Text == "0" || textBox2.Text == "0")
            {
                error();
            }

            else
            {
                int start = Convert.ToInt32(textBox1.Text);
                int fin = Convert.ToInt32(textBox2.Text);

                if (start > fin)
                {
                    error();
                }
                else
                {
                    progressBar1.Visible = true;
                    Display(start, fin);
                }
            }
        }

        public void Display(int start, int finish)                                      //and its function
        {
            int rangeSize = finish - start + 1;
            int[] numbers = new int[rangeSize];
            int[] maximumValues = new int[rangeSize];
            int[] iterationCounts = new int[rangeSize];

            progressBar1.Maximum = finish;
            progressBar1.Minimum = start;
            progressBar1.Value = start;

            for (int i = 0; i < rangeSize; i++)
            {
                int currentNumber = start + i;
                progressBar1.Value = currentNumber;
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

            listBox1.Items.Add("Number " + numbers[smallestIterationsIndex] + " has smallest amount of iterations: " + iterationCounts[smallestIterationsIndex] + ". Higheswt value: " + maximumValues[smallestIterationsIndex]);
            listBox1.Items.Add("Number " + numbers[largestIterationsIndex] + " has largest amount of iterations: " + iterationCounts[largestIterationsIndex] + ". Highest value: " + maximumValues[largestIterationsIndex]);
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)               //to put only integer
        {
            e.Handled = !char.IsNumber(e.KeyChar) && !char.IsControl(e.KeyChar);
        }

        private void textBox2_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = !char.IsNumber(e.KeyChar) && !char.IsControl(e.KeyChar);
        }

        private void textBox1_KeyUp(object sender, KeyEventArgs e)                         //to use enter to move to the next line
        {
            if ((e.KeyCode == Keys.Enter) || (e.KeyCode == Keys.Return))
            {
                this.SelectNextControl((Control)sender, true, true, true, true);
            }
        }
        private void error()
        {
            textBox1.Clear();
            textBox2.Clear();
            textBox1.PlaceholderText = "Error. Enter the correct value.";
            textBox2.PlaceholderText = "Error. Enter the correct value.";
        }

        private void textBox2_KeyDown(object sender, KeyEventArgs e)                       //enter
        {
            if (e.KeyCode == Keys.Enter)
                button1.PerformClick();
        }

        private void button2_Click(object sender, EventArgs e)                            //button clear
        {
            listBox1.Items.Clear();
        }
    }
}