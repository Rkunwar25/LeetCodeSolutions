class Solution(object):
    def sumZero(self, n):
        result = [i for i in range(1, n//2 + 1)] + [-i for i in range(1, n//2 + 1)]
        if n % 2 != 0:
            result.append(0)
        
        return result