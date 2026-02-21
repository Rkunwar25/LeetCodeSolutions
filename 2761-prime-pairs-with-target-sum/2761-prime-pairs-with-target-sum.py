class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n < 3:
            return []
        
        # Step 1: Build sieve up to n
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for multiple in range(i*i, n + 1, i):
                    sieve[multiple] = False
        
        # Step 2: Check pairs
        ans = []
        for p in range(2, n // 2 + 1):
            if sieve[p] and sieve[n - p]:
                ans.append([p, n - p])
        
        return ans