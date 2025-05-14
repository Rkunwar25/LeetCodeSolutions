class Solution(object):
    def countElements(self, nums):
        mn=min(nums)
        mx=max(nums)
        c=0
        for i in nums:
            if mn<i<mx:
                c+=1
        return c