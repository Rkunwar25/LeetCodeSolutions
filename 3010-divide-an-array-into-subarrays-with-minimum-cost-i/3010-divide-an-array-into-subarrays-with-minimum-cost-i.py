class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # First element is always included
        first = nums[0]
        
        # Get two smallest from remaining elements
        rest = sorted(nums[1:])
        
        return first + rest[0] + rest[1]
