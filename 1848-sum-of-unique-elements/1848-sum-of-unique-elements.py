class Solution(object):
    def sumOfUnique(self, nums):
        c=Counter(nums)
        s=0
        for i,j in c.items():
            if j==1:
                s+=i
        return s