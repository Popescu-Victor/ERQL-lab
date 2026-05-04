#include <stdio.h>
#include <stdlib.h>

// Allocate a 2D matrix of given rows x cols
double **create_matrix(int rows, int cols) {
    double **matrix = (double **)malloc(rows * sizeof(double *));
    for (int i = 0; i < rows; i++) {
        matrix[i] = (double *)calloc(cols, sizeof(double));
    }
    return matrix;
}

// Free a previously allocated 2D matrix
void free_matrix(double **matrix, int rows) {
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

// Dot multiply: result = a (rows_a x cols_a) * b (cols_a x cols_b)
double **dot_multiply(double **a, double **b, int rows_a, int cols_a, int cols_b) {
    double **result = create_matrix(rows_a, cols_b);

    for (int i = 0; i < rows_a; i++) {
        for (int j = 0; j < cols_b; j++) {
            for (int k = 0; k < cols_a; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    return result;
}

void print_matrix(const char *name, double **matrix, int rows, int cols) {
    printf("%s:\n", name);
    for (int i = 0; i < rows; i++) {
        printf("  [");
        for (int j = 0; j < cols; j++) {
            printf("%6.1f", matrix[i][j]);
            if (j < cols - 1) printf(", ");
        }
        printf("]\n");
    }
    printf("\n");
}

int main() {
    // Matrix A: 3x2
    int rows_a = 3, cols_a = 2;
    double **matrix_a = create_matrix(rows_a, cols_a);
    double init_a[3][2] = {
        {1.0, 2.0},
        {3.0, 4.0},
        {5.0, 6.0}
    };
    for (int i = 0; i < rows_a; i++)
        for (int j = 0; j < cols_a; j++)
            matrix_a[i][j] = init_a[i][j];

    // Matrix B: 2x3
    int rows_b = 2, cols_b = 3;
    double **matrix_b = create_matrix(rows_b, cols_b);
    double init_b[2][3] = {
        {7.0,  8.0,  9.0},
        {10.0, 11.0, 12.0}
    };
    for (int i = 0; i < rows_b; i++)
        for (int j = 0; j < cols_b; j++)
            matrix_b[i][j] = init_b[i][j];

    print_matrix("Matrix A (3x2)", matrix_a, rows_a, cols_a);
    print_matrix("Matrix B (2x3)", matrix_b, rows_b, cols_b);

    // cols_a must equal rows_b for valid dot product
    double **result = dot_multiply(matrix_a, matrix_b, rows_a, cols_a, cols_b);
    print_matrix("Result A · B (3x3)", result, rows_a, cols_b);

    // Clean up
    free_matrix(matrix_a, rows_a);
    free_matrix(matrix_b, rows_b);
    free_matrix(result, rows_a);

    return 0;
}
