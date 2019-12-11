#include <iostream>
#include <string>
using namespace std;


int main()
{
	string op;

	cout << "enter the word 'egg'\n\n";

	while (true) {
		cin >> op;
		if (op == "egg")
			cout << "Thanks\n\n";
		else if (op == "stop" || op == "s")
			break;
		else
			cout << "Fuck you.\n\n";
	}
	cout << "You have successfully exited the program.";
	return 0;
}

/*
cout << "Please enter your first number: ";
cin >> in1;

cout << endl << "Please enter your second number: ";
cin >> in2;

fin = in1 + in2;
cout << endl << in1 << " + " << in2 << " = " << fin;

*/


/*

for ( initial statement; condition; increment or loop control variable) {
  statement(s);
}

*/