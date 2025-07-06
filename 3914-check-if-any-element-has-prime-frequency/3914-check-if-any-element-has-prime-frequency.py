class Solution(object):
    def checkPrimeFrequency(self, nums):
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
              if n % i == 0 or n % (i + 2) == 0:
                return False
              i += 6
            return True
        
        c=Counter(nums)
        for i in c:
            if is_prime(c[i]):
                return True
        return False