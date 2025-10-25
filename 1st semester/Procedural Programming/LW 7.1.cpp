#include <iostream>
using namespace std;
void Atrap(float& sum, float& height, float& Area);
float Atrap(float& x, float& y);
int main()
{
	float a;//1st base
	float b;//2nd base
	float h;//height
	float s;
	cout << "Enter 1st base: ";
	cin >> a;
	cout << "Enter 2nd base: ";
	cin >> b;
	cout << "Enter height: ";
	cin >> h;
	float sum = Atrap(a, b);
	Atrap(sum, h, s);
	return 0;
}

float Atrap(float& x, float& y)
{
	float sum;
	sum = (x + y) / 2;
	return sum;
}
void Atrap(float& sum, float& height, float& Area)
{
	Area = sum * height;
	cout << "Area of trapezoid: " << Area;

}
