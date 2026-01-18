class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count=0
        l=sorted(nums)
        for i in nums:
            if l.count(i)>=2:
                l.remove(i)
                l.remove(i)
                count+=1
        return [count,len(l)]