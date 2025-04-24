class Solution(object):
    def diagonalSum(self, mat):
        n = len(mat)  # Get the size of the square matrix
        total_sum = 0
        
        for i in range(n):
            total_sum += mat[i][i]  # Primary diagonal
            total_sum += mat[i][n - i - 1]  # Secondary diagonal
        
        # If the matrix size is odd, subtract the center element to avoid double counting
        if n % 2 == 1:
            total_sum -= mat[n // 2][n // 2]
        
        return total_sum     
        