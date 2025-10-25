#include <iostream>
using namespace std;

void comparison(int& a, int& b);

int main()
{
	int x, y;
	cout << "Write first numbers to compare"<<endl;
	cin >> x;
	cout << "Write second numbers to compare" << endl;
	cin >> y;
	comparison(x, y);
}

void comparison(int& a, int& b)
{
	if (a > b)
	{
		cout << "Number " << a << " greater than " << b;
	}
	else if (b > a)
	{
		cout << "Number " << b << " greater than " << a;
	}
	else if (a == b)
	{
		cout << "Number " << a << " and " << b << " are equal.";
	}
}
