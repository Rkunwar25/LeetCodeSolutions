class Solution(object):
    def averageValue(self, nums):
        tot=0
        count=0
        for i in nums:
            if i%6==0:
                tot+=i
                count+=1
        if count!=0:
            return tot/count
        return 0