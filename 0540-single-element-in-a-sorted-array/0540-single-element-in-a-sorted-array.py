class Solution(object):
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # Make sure mid is even
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]
