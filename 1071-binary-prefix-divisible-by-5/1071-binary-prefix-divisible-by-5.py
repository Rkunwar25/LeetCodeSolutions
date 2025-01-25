class Solution(object):
    def prefixesDivBy5(self, nums):
        l=[]
        if nums[0]%5==0:
            l.append(True)
        else:
            l.append(False)
        s=str(nums[0])
        for i in range(1,len(nums)):
            s+=str(nums[i])
            r=int(s,2)
            if r%5==0:
                l.append(True)
            else:
                l.append(False)
        return l