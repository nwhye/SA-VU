#include<iostream>
#include<set>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
    set <int> s1 = {1,2,3};
    set <int> s0 = {1,2,3};
    vector <int> s2;

    set <int>::iterator it;

    set_difference(s1.begin(), s1.end(), s0.begin(), s0.end(), back_inserter(s2));

    cout << "set A = {";

    for (it = s1.begin(); it != s1.end(); it++) {
        cout << ' ' << *it;
    }

    cout << " }\n";

    cout << "set A / A = {";

    for (int x : s2) {
        cout << ' ' << x;
    }

    cout << " }\n";

    cout << "A / A = O";

}
