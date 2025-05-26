class Solution(object):
    def isSameAfterReversals(self, num):
        reversed1=int(str(num)[::-1])
        reversed2=int(str(reversed1)[::-1])
        return reversed2==num