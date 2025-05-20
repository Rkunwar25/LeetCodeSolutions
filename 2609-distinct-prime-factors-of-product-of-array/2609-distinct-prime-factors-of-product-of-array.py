class Solution(object):
    def distinctPrimeFactors(self, nums):
        def get_prime_factors(n):
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            i = 3
            while i * i <= n:
                while n % i == 0:
                    factors.add(i)
                    n //= i
                i += 2
            if n > 2:
                factors.add(n)
            return factors

        all_factors = set()
        for num in nums:
            all_factors |= get_prime_factors(num)  # union of sets

        return len(all_factors)
