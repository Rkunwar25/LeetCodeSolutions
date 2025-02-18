class Solution(object):
    def thirdMax(self, nums):
        # Use a set to get unique values
        unique_nums = sorted(set(nums), reverse=True)

        # Return third max if possible; otherwise, return max
        return unique_nums[2] if len(unique_nums) >= 3 else unique_nums[0]
