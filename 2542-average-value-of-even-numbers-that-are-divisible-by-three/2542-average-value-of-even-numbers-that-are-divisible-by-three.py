class Solution(object):
    def averageValue(self, nums):
        l=[]
        for i in nums:
            if i%2==0 and i%3==0:
                l.append(i)
        if l:
            return sum(l)/len(l)
        else:
            return 0