class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1  
        INT_MIN = -2**31 
        if dividend//divisor>INT_MAX:
            return INT_MAX
        if dividend//divisor<INT_MIN:
            return INT_MIN
        if dividend==0:
            return 0
        if (dividend<0 and divisor<0) or (dividend>0 and divisor>0):
            return dividend//divisor
        if dividend<0 or divisor<0:
            return -1*(abs(dividend)//abs(divisor))