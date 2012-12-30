#include <iostream>

using namespace std;

int main()
{
	//cerr << "chert" << endl;
	long long max; cin >> max;

	long long s = 0, e = max + 1;

	while (e - s > 1)
	{
		long long m = (e + s) / 2;
		cout << m << endl;
		string res;
		cin >> res;
		//cerr << "responce to " << m << " is " << res << endl;
		if (res == "correct")
			break;
		else if (res == "high")
			e = m;
		else 
			s = m;
	}

	return 0;
}
