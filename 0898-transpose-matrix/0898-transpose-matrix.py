class Solution(object):
    def transpose(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        result = [[0] * rows for _ in range(cols)]  # New transposed matrix

        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]  # Swap rows and columns
        
        return result