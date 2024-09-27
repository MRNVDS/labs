#include <iostream>
using namespace std;

int main() {
    int S, h;
    cout << "Enter square and height of the pyramid, separated with space: ";
    cin >> S >> h;

    // Проверка корректности введенных значений
    if (S > 100 || S <= 0 || h > 100 || h <= 0) {
        cout << "S and h must be between 0 and 100";
    } else {
        // Вычисление объема пирамиды
        float res = static_cast<float>(S) * static_cast<float>(h) / 3;
        cout << "Volume of the pyramid: " << res;
    }

    return 0;
}