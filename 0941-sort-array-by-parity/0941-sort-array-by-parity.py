class Solution(object):
    def sortArrayByParity(self, nums):
        l=[]
        for i in nums:
            if i%2==0:
                l.append(i)
        for i in nums:
            if i%2!=0:
                l.append(i)
        return l
        