class Solution(object):
    def checkXMatrix(self, grid):
        flag=0
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if i==j or j==n-i-1:
                    if grid[i][j]==0:
                        flag=1
                        break
                else:
                    if grid[i][j]!=0:
                        flag=1
                        break
        return flag==0