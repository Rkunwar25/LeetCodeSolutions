class Solution(object):
    def getSum(self, a, b):
        MAX = 0x7FFFFFFF
        MASK = 0xFFFFFFFF
        while b != 0: 
           a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        return a if a <= MAX else ~(a ^ MASK)