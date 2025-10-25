#include <iostream>
using namespace std;
template<class T>
T frequency(T x, T y, T s)
{
	s = x / y;
	cout << "freguancy equal " << s;
	return 0;
}
int main()
{
	double a, b;
	double result{};
	cout << "Enter the number of times the event occurs" << endl;
	cin >> a;
	cout << "Enter the length of time" << endl;
	cin >> b;
	frequency(a, b,result);
}
