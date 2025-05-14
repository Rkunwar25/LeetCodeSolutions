class Solution(object):
    def maxFrequencyElements(self, nums):
        count=Counter(nums)
        c=[]
        c1=0
        for i,j in count.items():
            c.append(j)
        mx=max(c)
        for i,j in count.items():
            if mx==j:
                c1+=j
        return c1