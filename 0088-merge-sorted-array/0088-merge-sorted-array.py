class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums3=nums1[:m]        
        nums3.extend(nums2)
        nums3=sorted(nums3)
        for i in range(len(nums3)):
            nums1[i] = nums3[i]