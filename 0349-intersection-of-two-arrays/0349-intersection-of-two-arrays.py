class Solution(object):
    def intersection(self, nums1, nums2):
        # i=0
        # l=[]
        # while i<len(nums1) and i<len(nums2):
        #     if nums1[i] in nums2:
        #         l.append(nums1[i])                
        #     if nums2[i] in nums1:
        #         l.append(nums2[i])
        #     i+=1
        # l1=set(l)
        # l=list(l1)
        return list(set(nums1) & set(nums2))