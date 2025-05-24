class Solution(object):
    def modifiedMatrix(self, matrix):
        matrix=[list(row) for row in zip(*matrix)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==-1:
                    matrix[i][j]=max(matrix[i])
        matrix=[list(row) for row in zip(*matrix)]
        return matrix