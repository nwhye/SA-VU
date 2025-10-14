#include <iostream>
using namespace std;
int main()
{
	float a, b, c, d, e, sum;
	cout << "Enter price $: ";
	cin >> a >> b >> c >> d >> e;
	for (int i = 0; i < 5; i++)
	{
		int array[5] = { a, b, c, d, e };
		if (a || b || c || d || e > 0)
		{
			sum = array [i] * 0.21;
			cout << "VAT: " << sum << "$" << "\n";
		}
		else
		{
			cout << "Price can not be negative";
			break;
		}
	}

}
