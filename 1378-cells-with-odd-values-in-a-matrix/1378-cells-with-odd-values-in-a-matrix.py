# class Solution(object):
#     def oddCells(self, m, n, indices):
#         l=[[0]*n for _ in range(m)]
#         count=0
#         for i in indices:
#             r=i[0]
#             c=i[1]
#             print(r,c)
#             for j in range(n):
#                 l[r][j]+=1
                
#             for j in range(m):
#                 l[j][c]+=1
                
#         for i in l:
#             for j in range(len(i)):
#                 if i[j]%2!=0:
#                     count+=1
#         return count
class Solution(object):
    def oddCells(self, m, n, indices):
        row = [0] * m
        col = [0] * n
        
        # Track row and column increments
        for r, c in indices:
            row[r] += 1
            col[c] += 1
        
        # Count the number of odd rows and odd columns
        odd_rows = sum(1 for r in row if r % 2 == 1)
        odd_cols = sum(1 for c in col if c % 2 == 1)
        
        # Compute the number of odd cells
        return (odd_rows * (n - odd_cols)) + ((m - odd_rows) * odd_cols)
        