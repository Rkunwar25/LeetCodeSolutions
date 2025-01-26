class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return "0"
        s=""
        x=abs(num)
        # r=0
        while x:
            s=str(x%7)+s
            x//=7
        if num<0:
            s="-"+s
        return s