#include <iostream>
using namespace std;

int main()
{
	int a;
	int sum = 0;
	cout << "Enter only positive numbers: ";
	for (int i = 0;; i++)
	{
		cin >> a;
		if (a > 0)
		{
			sum = a + sum;
			cout << "The sum is: " << sum << "\n";
		}
		else
		{
			cout << "Entered number is not positive or is zero";
			break;
		}
	}

}
