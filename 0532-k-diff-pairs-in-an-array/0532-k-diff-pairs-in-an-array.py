class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    if [nums[i],nums[j]] not in c:
                        c.append([nums[i],nums[j]])
        return len(c)