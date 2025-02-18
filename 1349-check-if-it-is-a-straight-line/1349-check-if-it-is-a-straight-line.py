class Solution(object):
    def checkStraightLine(self, coordinates):
        # Extract first two points to compute initial differences
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        # Compute slope components (avoid division)
        dx = x1 - x0
        dy = y1 - y0
        
        # Check consistency for remaining points
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            
            # Cross multiplication to avoid division
            if (y - y0) * dx != (x - x0) * dy:
                return False
        
        return True
