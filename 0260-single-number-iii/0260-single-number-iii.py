class Solution(object):
    def singleNumber(self, nums):
       count=Counter(nums)
       l=[]
       for i,j in count.items():
          if j==1:
             l.append(i)
       return l