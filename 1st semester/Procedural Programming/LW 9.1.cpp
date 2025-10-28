#include <iostream>
using namespace std;

int main() {

    int numbers[5]{};
    cout << "Enter 5 numbers: " << endl;
    for (int i = 0; i < 5; i++) {
        cin >> numbers[i];
    }
    cout << "The numbers are: ";
    for (int n = 0; n < 5; n++) {
        cout << numbers[n] << "  ";
    }
    int sum;
    sum = numbers[0] + numbers[4];
    cout << endl<< "The sum of the first and last number is: " << sum;
    return 0;
}
