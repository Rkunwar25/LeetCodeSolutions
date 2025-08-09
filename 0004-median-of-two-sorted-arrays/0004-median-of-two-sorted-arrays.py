class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)  # simpler than extend + sort
        n = len(merged)
        mid = n // 2
        if n % 2:
            return merged[mid]
        else:
            return (merged[mid - 1] + merged[mid]) / 2.0
