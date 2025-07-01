class Solution(object):
    def dominantIndex(self, nums):
        l=list(nums)
        l.sort(reverse=True)
        flag=0
        for i in range(1,len(l)):
            if l[0]>=(2*l[i]):
                flag=0
            else:
                flag=1
                break
        return nums.index(l[0]) if flag==0 else -1