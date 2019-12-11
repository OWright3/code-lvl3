#include <iostream>
#include <string>
using namespace std;


int main() {
    string bob;


    cout << "enter 1, 2 or 3\n";
    cin >> bob;


    if (bob == "1") {
        cout << "\nthing one";
        return 0;
    }
    else if (bob == "2") {
        cout << "\nthing two";
        return 0;
    }
    else if (bob == "3") {
        cout << "\nthing three";
        return 0;
    }
    else {
        cout << "the option '" << bob << "' is invalid. Please enter 1, 2 or 3";
        return 0;
    }
}
