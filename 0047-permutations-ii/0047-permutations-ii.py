class Solution(object):
    def permuteUnique(self, nums):
        return list(set(permutations(nums)))
