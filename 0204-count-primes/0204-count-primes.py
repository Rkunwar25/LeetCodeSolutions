class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0:2] = [False, False]

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        c=0
        for i in is_prime:
            if i==True:
                c+=1
        return c