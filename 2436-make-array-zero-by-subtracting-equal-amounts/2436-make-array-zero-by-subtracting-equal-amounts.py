class Solution(object):
    def minimumOperations(self, nums):
                return len(set(x for x in nums if x > 0))
