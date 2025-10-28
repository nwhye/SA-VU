#include <iostream>
using namespace std;
int main() {
    int arr[10]{};
    float ave = 0;
    int sum = 0;
    for (int i = 0; i < 10; i++)
    {
        arr[i] = rand() % 100;
    }
    for (int i = 0; i < 10; i++)
    {
        cout << arr[i] << "  ";
    }
    for (int i = 0; i < 10; i++) {
        sum += arr[i];
    }
    ave = (float)sum / 10;
    cout << endl<< "Average = " << ave;
    return 0;
}
