#include <iostream>
using namespace std;

int countMultOfNumb(int n) {
    /*int res = 1;
    while (n > 0) {
        int a = n % 10;
        if (a != 0) { 
            res *= a;
        }
        n /= 10;
    }
    return res; */
    int res = 1;
    while(n > 0)
    {
        res *= n % 10;
        n /= 10;
    }
    return res;
}

int main() {
    cout << "To stop enter queue, enter 0" << endl;
    int i;
    int max = -2147483648; 
    int maxIndex = -1;     
    int sum = 0;           
    int index = 0;         

    while (cin >> i) {
        if (i == 0) {
            break; 
        }

        
        if (i < 0 && i % 7 == 0) {
            sum += i; 
            if (i > max) {
                max = i;       
                maxIndex = index; 
            }
        }
        index++; 
    }

    
    cout << "Sum of negative numbers divisible by 7: " << sum << endl;
    if (maxIndex != -1) {
        cout << "Max negative number divisible by 7: " << max << endl;
        cout << "Index of max value: " << maxIndex << endl;
    } else {
        cout << "No negative numbers divisible by 7 were found." << endl;
    }

    
    int n;
    cout << "Enter a natural number N (N < 10^9): ";
    cin >> n;
    if (n > 0 && n < 1000000000) {
        cout << "Product of digits in N: " << countMultOfNumb(n) << endl;
    } else {
        cout << "Invalid input. N must be a natural number less than 10^9." << endl;
    }

    return 0;
}