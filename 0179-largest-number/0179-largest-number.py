class Solution(object):
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(lambda x, y: 1 if x+y < y+x else -1))
        return "0" if nums[0] == "0" else "".join(nums)