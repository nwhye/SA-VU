#include <iostream>
using namespace std;

int main()
{
	string word;
	cout << "Enter the word: ";
	cin >> word;
	for (int i = 0; i < word.length(); i++)
	{

		if (i == 2) {
			if (word.length() == 3) {
				cout << "1";
			}
			else {
				cout << "1" << "\n";//changes third letter to "1"
			}
			continue;
		}
		if (i == word.length() - 1)
		{
			cout << word[i];
		}
		else {
			cout << word[i] << "\n";
		}
	}
	return 0;
