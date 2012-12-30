#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char *argv[])
{
	ifstream fin(argv[1]);
	long long n, tmp;
	fin >> n;

	for (int i = 0; i < 74; i++)
	{
		cin >> tmp;
		if (tmp == n)
		{
			cout << "correct" << endl;
			cerr << 100 << endl;
			return 0;
		}
		else if (tmp > n)
			cout << "high" << endl;
		else
			cout << "low" << endl;
	}

	cerr << 0 << endl;
	return 0;
}     
