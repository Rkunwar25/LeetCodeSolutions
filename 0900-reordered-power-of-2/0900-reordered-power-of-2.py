class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Sort digits of n
        target = sorted(str(n))
        
        # Check all powers of 2 up to 10^9
        for i in range(31):  # 2^30 = 1073741824 > 10^9
            if sorted(str(1 << i)) == target:
                return True
        return False
