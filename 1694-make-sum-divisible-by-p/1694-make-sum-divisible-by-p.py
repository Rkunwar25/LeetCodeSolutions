class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0

        mod_map = {0: -1}
        prefix = 0
        res = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            required = (prefix - target + p) % p
            if required in mod_map:
                res = min(res, i - mod_map[required])
            mod_map[prefix] = i

        return res if res < len(nums) else -1
