class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        result = []
        
        left, right = 1, k + 1
        
        # Create zig-zag for first k+1 numbers
        while left <= right:
            result.append(left)
            left += 1
            
            if left <= right:
                result.append(right)
                right -= 1
        
        # Append remaining numbers
        for num in range(k + 2, n + 1):
            result.append(num)
        
        return result