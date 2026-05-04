object MatrixDot {

  def dotMultiply(a: Array[Array[Double]], b: Array[Array[Double]]): Array[Array[Double]] = {
    val rowsA = a.length
    val colsA = a(0).length
    val rowsB = b.length
    val colsB = b(0).length

    require(colsA == rowsB,
      s"Incompatible dimensions: A is ${rowsA}x${colsA}, B is ${rowsB}x${colsB} (cols of A must equal rows of B)")

    Array.tabulate(rowsA, colsB) { (i, j) =>
      (0 until colsA).map(k => a(i)(k) * b(k)(j)).sum
    }
  }

  def printMatrix(name: String, matrix: Array[Array[Double]]): Unit = {
    println(s"$name:")
    matrix.foreach { row =>
      val formatted = row.map(v => f"$v%6.1f").mkString(", ")
      println(s"  [$formatted]")
    }
    println()
  }

  def main(args: Array[String]): Unit = {
    // Matrix A: 3x2
    val matrixA = Array(
      Array(1.0, 2.0),
      Array(3.0, 4.0),
      Array(5.0, 6.0)
    )

    // Matrix B: 2x3
    val matrixB = Array(
      Array(7.0,  8.0,  9.0),
      Array(10.0, 11.0, 12.0)
    )

    printMatrix("Matrix A (3x2)", matrixA)
    printMatrix("Matrix B (2x3)", matrixB)

    val result = dotMultiply(matrixA, matrixB)
    printMatrix("Result A · B (3x3)", result)
  }
}
