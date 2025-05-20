from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution(object):
    def isGoodArray(self, nums):
        gcd_all = reduce(gcd, nums)
        return gcd_all == 1
