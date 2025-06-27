class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        l=[]
        for i in nums1:
            c=0
            for j in nums2[nums2.index(i):]:
                if j>i:
                    l.append(j)
                    c=1
                    break
            if c==0:
                l.append(-1)
        return l 