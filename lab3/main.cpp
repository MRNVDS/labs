#include <iostream>
using namespace std;

string binary(int n) {
    if (n == 0) return "0"; 
    string binary = "";
    while (n > 0) {
        binary = (n % 2 == 0 ? "0" : "1") + binary;
        n /= 2;
    }
    return binary;
}

int main() {
    int x, i;
    cout << "Enter two integers (x and i): ";
    cin >> x >> i;

    string binaryRepresentation = binary(x); 
    if (i >= 0 && i < binaryRepresentation.length()) {
        cout << "The " << i << "-th bit of " << x << " in binary is: " << binaryRepresentation[i] << endl;
    } else {
        cout << "Error: i is out of bounds for the binary representation of x." << endl;
    }

    return 0;
} 
