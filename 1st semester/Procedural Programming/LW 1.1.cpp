#include<iostream>
using namespace std;
int main()
{
    float x, c;
cout << "Write your temperature in Celsius: ";
cin >> x;
c = (x*9/5) + 32;
cout << "In Farenheit your temperature will be: " << c;
}


#include<iostream>
using namespace std;
int main()
{
    int x;
cout << "Write the year: ";
cin >> x;
if (x % 4) {
    cout << "The year is common";
    }
else {cout << "The year is leap";
}
}
