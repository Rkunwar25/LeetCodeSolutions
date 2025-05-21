class Solution(object):
    def minNumber(self, nums1, nums2):
        l=set(nums1) & set(nums2)
        if l:
            return min(l)
        n=min(nums1)
        m=min(nums2)
        return min(n*10+m,m*10+n)