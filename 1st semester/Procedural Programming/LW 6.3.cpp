#include <iostream>
using namespace std;

void analyse(int& a);

int main()
{
	int x;
	cout << "" << endl;
	cin >> x;
	analyse(x);
}

void analyse(int& a)
{
	if (a % 2 == 0)
	{
		cout << "Even";
	}
	else
	{
		cout << "Odd";
	}
}
