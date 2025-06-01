class Solution(object):
    def generateTheString(self, n):
        if n%2!=0:
            return n*"p"
        else:
            return "p"+(n-1)*"q"