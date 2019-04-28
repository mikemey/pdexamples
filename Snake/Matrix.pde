// author: "Code Bullet" (https://github.com/Code-Bullet/SnakeFusion/blob/master/SmartSnakesCombine/Matrix.pde)

class Matrix {
  int rows, cols;
  float[][] matrix;

  Matrix(int r, int c) {
    rows = r;
    cols = c;
    matrix = new float[rows][cols];
  }

  Matrix dot(Matrix n) {
    Matrix result = new Matrix(rows, n.cols);
    if (cols == n.rows) {
      for (int i = 0; i < rows; i++) {
        for (int j = 0; j < n.cols; j++) {
          float sum = 0;
          for (int k = 0; k < cols; k++) {
            sum += matrix[i][k] * n.matrix[k][j];
          }
          result.matrix[i][j] = sum;
        }
      }
    }
    return result;
  }

  void randomize() {
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        matrix[i][j] = random(-1, 1);
      }
    }
  }

  Matrix singleColumnMatrixFromArray(float[] arr) {
    Matrix m = new Matrix(arr.length, 1);
    for (int i = 0; i < arr.length; i++) {
      m.matrix[i][0] = arr[i];
    }
    return m;
  }

  void fromArray(float[] arr) {
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        matrix[i][j] =  arr[j + i * cols];
      }
    }
  }

  float[] toArray() {
    float[] arr = new float[rows * cols];
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        arr[j + i * cols] = matrix[i][j];
      }
    }
    return arr;
  }

  Matrix addBias() {
    Matrix m = new Matrix(rows + 1, 1);
    for (int i = 0; i < rows; i++) {
      m.matrix[i][0] = matrix[i][0];
    }
    m.matrix[rows][0] = 1;
    return m;
  }

  Matrix activate() {
    Matrix m = new Matrix(rows, cols);
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        m.matrix[i][j] = sigmoid(matrix[i][j]);
      }
    }
    return m;
  }

  float sigmoid(float x) {
    return 1 / (1 + pow((float) Math.E, -x));
  }

  void mutate(float mutationRate) {
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        if (shouldMutate(mutationRate)) {
          matrix[i][j] = mutateField(matrix[i][j]);
        }
      }
    }
  }

  private boolean shouldMutate(float mutationRate) {
    return random(1) < mutationRate;
  }

  private float mutateField(float val) {
    float newVal = val + randomGaussian() / 5;
    newVal = Math.min(1, newVal);
    return Math.max(-1, newVal);
  }

  Matrix crossover(Matrix partner) {
    Matrix child = new Matrix(rows, cols);
    int cutoffCol = floor(random(cols));
    int cutoffRow = floor(random(rows));
    for (int i =0; i<rows; i++) {
      for (int j = 0; j<cols; j++) {
        if (i < cutoffRow || ( i == cutoffRow && j < cutoffCol)) {
          child.matrix[i][j] = matrix[i][j];
        } else {
          child.matrix[i][j] = partner.matrix[i][j];
        }
      }
    }
    return child;
  }
}
