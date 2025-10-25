#include <iostream>
using namespace std;

int main()
{
	int a;
	int s = 0;
	int v;
	cout << "Enter your number: ";
	cin >> a;
	while (s < a)
	{
		s++;
		v = s * s * s;
		cout << v << ",";
	}
	cout << "\b";
}
