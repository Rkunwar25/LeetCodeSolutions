class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        if n%2!=0:        
            return nums1[n//2]
        else:
            pos=n//2
            return (nums1[pos-1]+nums1[pos])/2.0
        