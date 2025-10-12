#include <iostream>
using namespace std;
int main()
{
	int a;
	cout << "enter positive number: ";
	cin >> a;
	if (a % 2 == 0) {
		while (a > 0) {
			cout << a << "\n";
			a = a - 2;
		}
	}
	if (a > 0) {
		a = a - 1;
		while (a > 0) {
			cout << a << "\n";
			a = a - 2;
		}
	}
	else (a <= 0); {
		cout << "you'r number less or egual zero";
		return 0;
	}
}
