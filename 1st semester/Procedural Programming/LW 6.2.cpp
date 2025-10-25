#include <iostream>
using namespace std;

void counting(int& a, int& b);

int main()
{
	int number, power, result;
	cout << "choose number"<<endl;
	cin >> number;
	cout << "choose power" << endl;
	cin >> power;
	counting(number,power);
}

void counting(int& a, int& b)
{
	int s = 1;
	int i = 0;
	while (i < b)
	{
		s = a * s;
		i++;
	}
	cout << s;
}
