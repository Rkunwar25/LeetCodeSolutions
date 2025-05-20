class Solution(object):
    def diagonalPrime(self, nums):
        def isPrime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        
        d=[nums[i][i] for i in range(len(nums))]
        od=[nums[i][len(nums)-1-i] for i in range(len(nums))]
        l=[i for i in d if isPrime(i)]
        l.extend([i for i in od if isPrime(i)])
        return max(l) if l else 0