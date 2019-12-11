#include <iostream>
#include <string>
#include <cmath>
using namespace std;


int main()
{
	int a, b, c;
	float fp, fn, disc;
	string s_text = "Please enter the equation of the quadratic\n";
	string a_text = "Enter A: ";
	string b_text = "Enter B: ";
	string c_text = "Enter C: ";

	
	cout << s_text << a_text; cin >> a;
	cout << b_text; cin >> b;
	cout << c_text; cin >> c;
	

	disc = pow(b, 2) - 4 * a * c;
	if (disc < 0) {
		cout << "Invalid input";
	}
	else if 

}