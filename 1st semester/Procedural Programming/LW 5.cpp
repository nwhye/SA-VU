using namespace std;

int main()
{
	char a;
	cout << "Solve the math problem 47 + 15 ..?.. 35 +5 by entering the sign"<<"\n";
	cin >> a;
	switch (a)
	{
	case'<':
		cout << "Wrong answer";
		break;
	case'>':
		cout << "Correct answer";
		break;
	case'=':
		cout << "Wrong answer";
		break;
	default:
		cout << "Error.Please enter another sign";
		break;
	}
}
