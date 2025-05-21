class Solution(object):
    def minNumber(self, nums1, nums2):
        l=list(set(nums1) & set(nums2))
        if l:
            return min(l)
        n=min(nums1)
        m=min(nums2)
        if n>m:
            return int(str(m)+str(n))
        else:
            return int(str(n)+str(m))