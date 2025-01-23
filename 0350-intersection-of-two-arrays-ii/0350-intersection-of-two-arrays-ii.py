class Solution(object):
    def intersect(self, nums1, nums2):
        i=0
        l=[]
        if len(nums1)<len(nums2):
            while i<len(nums1) :
                if nums1[i] in nums2:
                    l.append(nums1[i]) 
                    nums2.remove(nums1[i])               
                i+=1
        elif len(nums1)>len(nums2):
            while i<len(nums2):
                if nums2[i] in nums1:
                    l.append(nums2[i]) 
                    nums1.remove(nums2[i])               
                i+=1
        
        else:
            return list(set(nums1) & set(nums2))
        return l