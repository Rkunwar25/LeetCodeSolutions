class Solution(object):
    def findDisappearedNumbers(self, nums):
        l=len(nums)
        l1=[]
        nums=sorted(nums)
        l1=[i for i in range(1,l+1)]
        return list(set(l1)-set(nums))