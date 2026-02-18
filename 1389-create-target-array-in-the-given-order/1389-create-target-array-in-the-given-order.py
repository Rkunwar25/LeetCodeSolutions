class Solution:
    def createTargetArray(self, nums, index):
        ans = []
        
        for i in range(len(nums)):
            ans.insert(index[i], nums[i])
        
        return ans
