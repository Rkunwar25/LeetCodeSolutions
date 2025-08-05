class Solution(object):
    def spiralOrder(self, matrix):
        l = []
        if not matrix:
            return l
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from Left to Right
            for i in range(left, right + 1):
                l.append(matrix[top][i])
            top += 1
            
            # Traverse from Top to Bottom
            for i in range(top, bottom + 1):
                l.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # Traverse from Right to Left
                for i in range(right, left - 1, -1):
                    l.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # Traverse from Bottom to Top
                for i in range(bottom, top - 1, -1):
                    l.append(matrix[i][left])
                left += 1
        
        return l
