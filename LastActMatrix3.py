def sum_diagonals(matrix):
  """Calculates the sum of the elements on the diagonals of a square matrix.

  Args:
    matrix: A square matrix represented as a list of lists.

  Returns:
    The sum of the elements on the diagonals of the matrix.
  """

  diagonal_sum = 0
  rows = len(matrix)

  # Iterate over the elements on the principal diagonal (top-left to bottom-right).
  for i in range(rows):
    diagonal_sum += matrix[i][i]

  # If the matrix has odd dimensions, subtract the middle element 
  # to avoid counting it twice (for diagonals crossing in the middle).
  if rows % 2 != 0:
    diagonal_sum -= matrix[rows // 2][rows // 2]

  # Iterate over the elements on the secondary diagonal (top-right to bottom-left).
  for i in range(rows):
    diagonal_sum += matrix[i][rows - i - 1]

  return diagonal_sum

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_sum = sum_diagonals(matrix)
print("Sum of diagonals:", diagonal_sum)