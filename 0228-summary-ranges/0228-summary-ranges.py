class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = []
        if not nums:
            return []
        ln = [nums[0]]
        for i in range(1, len(nums)):
             if nums[i] - nums[i - 1] == 1:
                   ln.append(nums[i])
             else:
                   l.append(ln)
                   ln = [nums[i]]
        l.append(ln)
        nl=[]
        for num in l:
            if len(num)!=1:
                nl.append(str(num[0])+"->"+str(num[-1]))
            else:
                nl.append(str(num[0]))
        return nl