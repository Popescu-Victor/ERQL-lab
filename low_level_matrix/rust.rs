fn dot_multiply(a: &Vec<Vec<f64>>, b: &Vec<Vec<f64>>) -> Vec<Vec<f64>> {
    let rows_a = a.len();
    let cols_a = a[0].len();
    let cols_b = b[0].len();

    assert_eq!(cols_a, b.len(), "Incompatible matrix dimensions for dot multiplication");

    let mut result = vec![vec![0.0; cols_b]; rows_a];

    for i in 0..rows_a {
        for j in 0..cols_b {
            for k in 0..cols_a {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    result
}

fn print_matrix(name: &str, matrix: &Vec<Vec<f64>>) {
    println!("{}:", name);
    for row in matrix {
        let formatted: Vec<String> = row.iter().map(|x| format!("{:6.1}", x)).collect();
        println!("  [{}]", formatted.join(", "));
    }
    println!();
}

fn main() {
    // Matrix A: 3x2
    let matrix_a: Vec<Vec<f64>> = vec![
        vec![1.0, 2.0],
        vec![3.0, 4.0],
        vec![5.0, 6.0],
    ];

    // Matrix B: 2x3
    let matrix_b: Vec<Vec<f64>> = vec![
        vec![7.0, 8.0, 9.0],
        vec![10.0, 11.0, 12.0],
    ];

    print_matrix("Matrix A (3x2)", &matrix_a);
    print_matrix("Matrix B (2x3)", &matrix_b);

    // Result will be 3x3
    let result = dot_multiply(&matrix_a, &matrix_b);
    print_matrix("Result A · B (3x3)", &result);
}
