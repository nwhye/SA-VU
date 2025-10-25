#include <iostream>
using namespace std;
float Atrap(float& x, float& y, float& z, float& Area);
int main()
{
	float  a;
	float  b;
	float  h;
	float  s;
	cout << "Enter 1st base: ";
	cin >> a;
	cout << "Enter 2nd base: ";
	cin >> b;
	cout << "Enter height: ";
	cin >> h;
	float Area = Atrap(a, b, h, s);
	return 0;
}

float Atrap(float& x, float& y, float& z, float& Area)
{
	float sum;
	sum = (x + y) / 2;
	Area = sum * z;
	cout << "Area of trapezoid: " << Area;
	return Area;
}
