class Solution(object):
    def findDifference(self, nums1, nums2):
        l1=[]
        l2=[]
        l=[]
        for i in nums1:
            if i not in nums2 and i not in l1:
                l1.append(i)
        for i in nums2:
            if i not in nums1 and i not in l2:
                l2.append(i)
        l.append(l1)
        l.append(l2)
        return l