class Solution(object):
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        nums.sort(reverse=True, key=lambda x: x*10)
        result = ''.join(nums)
        return result if result[0] != '0' else '0'