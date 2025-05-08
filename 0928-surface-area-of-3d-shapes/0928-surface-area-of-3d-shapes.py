class Solution(object):
    def surfaceArea(self, grid):
        n = len(grid)
        total_area = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    # Add the top and bottom surface area
                    total_area += 2 + (grid[i][j] * 4)
                    
                    # Subtract the overlapping faces with the top neighbor
                    if i > 0:
                        total_area -= min(grid[i][j], grid[i - 1][j]) * 2
                    
                    # Subtract the overlapping faces with the left neighbor
                    if j > 0:
                        total_area -= min(grid[i][j], grid[i][j - 1]) * 2
        
        return total_area
