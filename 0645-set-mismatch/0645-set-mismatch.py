class Solution(object):
    def findErrorNums(self, nums):
        l=[i for i in range(1,len(nums)+1)]
        l1=list(set(l)-set(nums))
        c=Counter(nums)
        c1=0
        for i,j in c.items():
            if j==2:
                c1=i
                break
        l1.append(c1)
        l1.reverse()
        return l1