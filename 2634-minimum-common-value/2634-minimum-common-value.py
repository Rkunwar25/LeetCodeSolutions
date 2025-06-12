class Solution(object):
    def getCommon(self, nums1, nums2):
        l=list(set(nums1)&set(nums2))
        return min(l) if l else -1