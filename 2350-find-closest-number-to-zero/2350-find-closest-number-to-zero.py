class Solution(object):
    def findClosestNumber(self, nums):
        closest = float('inf')
        closest_val = 0
        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest_val):
                closest = num
        
        return closest