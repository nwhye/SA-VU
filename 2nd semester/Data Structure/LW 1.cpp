#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<string> students =
    { "Ivan Kapusta", "Daniil Arbatov", "Anna Kutova", "Hanna Asiadouskaya", "Artem Shymko"};

    vector<int> age =
    { 18, 17, 19, 20, 18 };

    int indx = distance(age.begin(), min_element(age.begin(), age.end()));

        cout << "The youngest student is " << students[indx];

    return 0;
}
