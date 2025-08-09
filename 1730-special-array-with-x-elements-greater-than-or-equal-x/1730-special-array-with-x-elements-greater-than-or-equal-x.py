class Solution(object):
    def specialArray(self, nums):
        n = len(nums)
        for x in range(n + 1):  # x can be 0 to n
            count = sum(num >= x for num in nums)
            if count == x:
                return x
        return -1
