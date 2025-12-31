class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        if target == 0:
            return True
        
        import math
        return target % math.gcd(x, y) == 0