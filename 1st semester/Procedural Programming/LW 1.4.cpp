#include<iostream>
using namespace std;
int main()
{
    int x, y, a;
cout << "Write your 1st number: ";
cin >> x;
cout << "Write your 2nd number: ";
cin >> y;
if (x > 0 && y > 0) {
    a = 1;
}
else if (x < 0 && y > 0) {
    a = 2;
}
else if (x < 0 && y < 0) {
    a = 3;
}
else if (x > 0 && y < 0) {
    a = 4;
}
else {
    cout << "The point is located at axis, not in exact quadrant";
    return 0;}
cout << "The point is located at " << a << " quadrant";
}
