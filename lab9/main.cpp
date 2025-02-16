#include <iostream>
#include <bitset>

using namespace std;

int main() {
    int n;
    cin >> n;
    int *ptr = &n;
    unsigned char* bytePtr = reinterpret_cast<unsigned char*>(ptr);

    for (int i = 0; i < sizeof(n); i++) {
            cout << "Address: " << ptr + i
                << ", value (bin): " << bitset<8>(*(bytePtr + i))
                << " value:" << static_cast<int>(*(bytePtr + i))
                << endl;
        }

    return 0;
}