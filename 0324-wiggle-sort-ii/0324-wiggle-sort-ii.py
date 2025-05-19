class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        n = len(nums)
        half = (n + 1) // 2
        small = nums[:half][::-1]  # smaller half reversed
        large = nums[half:][::-1]  # larger half reversed
     
        nums[::2] = small  # even indices
        nums[1::2] = large # odd indices