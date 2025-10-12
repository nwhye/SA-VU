#include<iostream>
using namespace std;
int main()
{
    int x, y, z, a;
cout << "Write your 1st number: ";
cin >> x;
cout << "Write your 2nd number: ";
cin >> y;
cout << "Write your 3rd number: ";
cin >> z;
if ((x > y)&&(x > z)) {
    a = 1;
}
else if ((y > x)&&(y > z)) {
    a = 2;
}
else {
    a = 3;}
cout << "The largest number is " << a << " number";
}
