class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convert_to_base(n, base):
            if n == 0:
               return "0"
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""
            while n > 0:
                remainder = n % base
                result = digits[remainder] + result
                n //= base
            return result
        for i in range(2,n-1):
            a=convert_to_base(n, i)
            if a!=a[::-1]:
                return False
        return True