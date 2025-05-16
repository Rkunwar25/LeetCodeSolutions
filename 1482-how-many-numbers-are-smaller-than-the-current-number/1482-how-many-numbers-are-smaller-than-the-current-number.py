class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        l=[]
        for i in nums:
            c=0
            for j in nums:
                if j<i:
                    c+=1
            l.append(c)
        return l