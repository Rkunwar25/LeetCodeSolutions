class Solution(object):
    def searchRange(self, nums, target):
        l=[]
        if target not in nums:
            return [-1,-1]
        if nums.count(target)==1:
            return [nums.index(target),nums.index(target)]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
                break
        for i in range(len(nums)-1,0,-1):
            if nums[i]==target:
                l.append(i)
                break
        return l
