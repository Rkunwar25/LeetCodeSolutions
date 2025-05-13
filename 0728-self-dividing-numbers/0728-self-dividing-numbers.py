class Solution(object):
    def selfDividingNumbers(self, left, right):
        def is_self_dividing(n):
            for digit in str(n):
                if digit == '0' or n % int(digit) != 0:
                    return False
            return True
        
        return [i for i in range(left, right + 1) if is_self_dividing(i)==True]