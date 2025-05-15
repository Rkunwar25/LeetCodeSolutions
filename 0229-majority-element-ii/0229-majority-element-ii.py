class Solution(object):
    def majorityElement(self, nums):
       l=[]
       count=Counter(nums)
       n=len(nums)
       for i,j in count.items():
          if j>n//3:
            l.append(i)
       return l