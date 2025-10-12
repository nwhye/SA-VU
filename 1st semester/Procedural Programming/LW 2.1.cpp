#include<iostream>
using namespace std;
int main()
{
    int a, b, c;
    cout <<"Write first angle: ";
    cin >> a;
    cout <<"Write second angle: ";
    cin >> b;
    cout <<"Write third angle: ";
    cin >> c;
    int sum = a + b + c;
    if (sum > 180) {
        cout << "You can't create triangle with such angles";
    }
    else if (sum <= 0) {
        cout <<"Angels of the triangle can't be less or equal 0";
    }
    else {
        cout <<"You can create triangle with such angles";
    }
}
