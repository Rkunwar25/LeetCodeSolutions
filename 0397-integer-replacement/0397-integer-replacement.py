class Solution(object):
    def integerReplacement(self, n):
        c = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                if n == 3 or (n & 2) == 0:
                    n -= 1
                else:
                    n += 1
            c += 1
        return c
