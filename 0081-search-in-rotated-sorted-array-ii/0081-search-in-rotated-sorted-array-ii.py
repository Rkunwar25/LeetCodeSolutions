class Solution(object):
    def search(self, nums, target):
        for i in nums:
            if i==target:
                return True
        return False