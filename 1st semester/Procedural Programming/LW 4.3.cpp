#include <iostream>
using namespace std;
int main()
{
	int num1, num2, nu1, nu2;
	int largestdivisor = 0;
	cout << "Enter the first number: ";
	cin >> num1;
	cout << "Enter the second number: ";
	cin >> num2;
	nu1 = num1;
	nu2 = num2;
	if (num1 < 0)
	{
		nu1 = num1 * (-1);
	}
	if (num2 < 0)
	{
		nu2 = num2 * (-1);;
	}
	if (nu1 < nu2)
	{
		swap(nu1, nu2);
	}
	for (int i = nu2; i > 0; i--)
	{
		if (nu1 % i == 0 && nu2 % i == 0)
		{
			largestdivisor = i;
			break;
		}
	}
	cout << "The largest divisor of " << num1 << " and " << num2 << " is " << largestdivisor;
	return 0;
}
