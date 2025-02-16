#include "functions.hpp"

using namespace std;
using namespace DataProcessing;

int main() {
    int n;
    cout << "Enter n ";
    cin >> n;

    res result = readData(n);
    vector<vector<int>> matrix = processData(result.max, result.min, result.matrix);
    writeData(matrix, n);

    return 0;
}
