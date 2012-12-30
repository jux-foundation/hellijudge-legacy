#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[])
{
	ifstream fin (argv[1]);
	int z, y;
	fin >> z;
	cin >> y;
	if(z == y)
	{
//		cerr << "Correct!" << endl;
		cerr << 100 << endl;
		return 0;
	}
//	cerr << "Wrong!" << endl;
	cerr << 0 << endl;
	return 0;
}
