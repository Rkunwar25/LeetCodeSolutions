class Solution(object):
    def decompressRLElist(self, nums):
        l=[]
        for i in range(0,len(nums),2):
            l.extend([nums[i+1]]*nums[i])
        return l
        