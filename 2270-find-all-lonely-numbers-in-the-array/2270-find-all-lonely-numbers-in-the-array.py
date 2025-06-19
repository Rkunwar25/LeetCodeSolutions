class Solution(object):
    def findLonely(self, nums):
        c=Counter(nums)
        s=set(nums)
        l=[]
        for i in c:
            if c[i]==1 and (i+1 not in s) and (i-1 not in s):
                l.append(i)
        return l