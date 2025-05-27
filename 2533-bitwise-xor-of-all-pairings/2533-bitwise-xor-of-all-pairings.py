class Solution(object):
    def xorAllNums(self, nums1, nums2):
        xor1 = reduce(xor, nums1, 0)
        xor2 = reduce(xor, nums2, 0)

        res = 0
        if len(nums2) % 2 == 1:
            res ^= xor1
        if len(nums1) % 2 == 1:
            res ^= xor2
        return res