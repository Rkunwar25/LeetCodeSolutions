class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        
        nums.sort()  # Sort the array in ascending order
        Avg = [(nums[i] + nums[-(i + 1)]) / 2 for i in range(len(nums) // 2)]
        return min(Avg)
