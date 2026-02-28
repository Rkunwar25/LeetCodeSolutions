class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD=10**9+7
        s=""
        for i in range(1,n+1):
            s+=bin(i)[2:]
        return int(s,2)%MOD