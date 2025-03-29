#include <iostream>
using namespace std;

int main() {
    // Fixed 2x2 matrices
    const int rows = 2, cols = 2;
    int A[rows][cols] = {{1, 2}, {3, 4}};
    int B[rows][cols] = {{5, 6}, {7, 8}};
    int C[rows][cols] = {{0, 0}, {0, 0}};

    // Matrix multiplication (2x2)
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            for (int k = 0; k < cols; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    // Print result (not needed for PIM translation)
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << C[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
