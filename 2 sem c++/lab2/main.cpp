#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

// ---------------------- TASK 1 -------------------------
// Recursive function to print numbers from a to b (inclusive).
void printRange(int a, int b) {
    if(a > b)
        return;
    cout << a << " ";  // print current number
    printRange(a + 1, b);
}

// ---------------------- TASK 2 -------------------------
// Partition function for quick sort
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];  // choose the last element as pivot
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if(arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);  // place pivot in its correct position
    return i + 1;  // return the pivot index
}

// Recursive quick sort function
void quickSort(vector<int>& arr, int low, int high) {
    if(low < high) {
        int p = partition(arr, low, high);
        quickSort(arr, low, p - 1);
        quickSort(arr, p + 1, high);
    }
}

// Bubble sort implementation
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if(arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// ---------------------- TASK 3 -------------------------
// Function to find the shortest path in the maze using BFS.
// Allowed moves: up, down, left, right, and the four diagonal directions.
int solveMaze(const vector<vector<char>>& maze, int n, int m) {
    int startX = -1, startY = -1;
    
    // 2D vector for storing the step count for each cell; initialize to -1 (unvisited)
    vector<vector<int>> dist(n, vector<int>(m, -1));

    // Find the starting cell 'S'
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if(maze[i][j] == 'S') {
                startX = i;
                startY = j;
                break;
            }
        }
        if(startX != -1)
            break;
    }
    
    if(startX == -1)  // if start cell not found, return -1
        return -1;
    
    // 8 possible movement directions: up, down, left, right and 4 diagonals
    int directions[8][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1} };
    
    queue<pair<int, int>> q;
    dist[startX][startY] = 0;  // starting cell distance is 0
    q.push({startX, startY});
    
    while(!q.empty()) {
        pair<int, int> current = q.front();
        q.pop();
        int x = current.first;
        int y = current.second;
        
        // If reached destination 'E', return the step count.
        if(maze[x][y] == 'E') {
            return dist[x][y];
        }
        
        // Explore all 8 directions.
        for(auto& d : directions) {
            int newX = x + d[0];
            int newY = y + d[1];
            // Check grid bounds.
            if(newX >= 0 && newX < n && newY >= 0 && newY < m) {
                // If the cell is unvisited and passable ('.' or 'E')
                if(dist[newX][newY] == -1 && (maze[newX][newY] == '.' || maze[newX][newY] == 'E')) {
                    dist[newX][newY] = dist[x][y] + 1;
                    q.push({newX, newY});
                }
            }
        }
    }
    
    return -1;  // if no path is found, return -1
}

int main() {
    // ---------------------- TASK 1 -------------------------
    cout << "Task 1: Recursive printing of numbers from A to B" << endl;
    int A, B;
    cout << "Enter A and B (1 <= A < B <= 100): ";
    cin >> A >> B;
    cout << "Numbers from " << A << " to " << B << ":" << endl;
    printRange(A, B);
    cout << "\n\n";
    
    // ---------------------- TASK 2 -------------------------
    cout << "Task 2: Sorting Algorithms" << endl;
    int numElements;
    cout << "Enter the number of elements to sort: ";
    cin >> numElements;
    
    vector<int> data(numElements);
    cout << "Enter " << numElements << " integers separated by spaces:" << endl;
    for (int i = 0; i < numElements; i++) {
        cin >> data[i];
    }
    
    // Creating copies of the input vector for each sorting algorithm.
    vector<int> dataQuick = data;
    vector<int> dataBubble = data;
    
    // Quick sort
    quickSort(dataQuick, 0, dataQuick.size() - 1);
    
    // Bubble sort
    bubbleSort(dataBubble);
    
    // Output results
    cout << "Quick sort result: ";
    for(auto num : dataQuick)
        cout << num << " ";
    cout << endl;
    
    cout << "Bubble sort result: ";
    for(auto num : dataBubble)
        cout << num << " ";
    cout << "\n\n";
    
    // ---------------------- TASK 3 -------------------------
    cout << "Task 3: Shortest path in the maze" << endl;
    int n, m;
    cout << "Enter the number of rows (N) and columns (M) of the maze (2 <= N, M <= 100): ";
    cin >> n >> m;
    
    cout << "Enter the maze, each of the " << n << " rows on a new line:" << endl;
    cout << "Allowed characters: '.' (walkable), '#' (obstacle), 'S' (start), 'E' (end)" << endl;
    
    vector<vector<char>> maze(n, vector<char>(m));
    for (int i = 0; i < n; i++) {
        string line;
        cin >> line;  // считываем строку без пробелов
        for (int j = 0; j < m && j < line.size(); j++) {
            maze[i][j] = line[j];
        }
    }
    
    // Output the maze for visualization
    cout << "Maze:" << endl;
    for(auto & row : maze) {
        for(auto cell : row)
            cout << cell << " ";
        cout << endl;
    }
    
    // Compute and output the minimal number of steps from S to E
    int steps = solveMaze(maze, n, m);
    cout << "Minimum number of steps from S to E: " << steps << endl;
    
    return 0;
}
