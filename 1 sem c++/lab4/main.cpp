#include <iostream>
using namespace std;

int main() {
    // Задача 1: Ввод натуральных чисел A, B и C
    int A, B, C;
    cout << "Enter natural numbers A, B, and C: ";
    cin >> A >> B >> C;

    if (B <= 0 || C <= 0) {
        cout << "Error: B and C must be natural numbers." << endl;
    } else {
        if (A % B == 0) {
            if (B > C) {
                cout << "Result: " << A / B + C << endl;
            } else {
                cout << "Result: " << A / B - C << endl;
            }
        } else {
            cout << "Result: " << (A + B) * C << endl;
        }
    }

    // Задача 2: Ввод дня недели
    int N;
    cout << "Enter the day of the week number (1-7): ";
    cin >> N;

    switch (N) {
        case 1:
            cout << "Monday" << endl;
            break;
        case 2:
            cout << "Tuesday" << endl;
            break;
        case 3:
            cout << "Wednesday" << endl;
            break;
        case 4:
            cout << "Thursday" << endl;
            break;
        case 5:
            cout << "Friday" << endl;
            break;
        case 6:
            cout << "Saturday" << endl;
            break;
        case 7:
            cout << "Sunday" << endl;
            break;
        default:
            cout << "Error: Invalid input. Please enter a number from 1 to 7." << endl;
            break;
    }

    // Задача 3: Проверка переменной x
    int x;
    cout << "Enter the value of x (-1 or 1): ";
    cin >> x;

    if (x == -1) {
        cout << "Negative number" << endl;
    } else if (x == 1) {
        cout << "Positive number" << endl;
    } else {
        cout << "Error: x can only take values -1 or 1." << endl;
    }

    return 0;
}