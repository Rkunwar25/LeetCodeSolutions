class Solution(object):
    def findDuplicates(self, nums):
        count=Counter(nums)
        # l=[i for i,j in count.items() if j==2]
        return [num for num, freq in count.items() if freq == 2]