class Solution(object):
    def maxProduct(self, n):
        l=str(n)
        dig=[int(i) for i in l]
        dig.sort(reverse=True)
        return dig[0]*dig[1]