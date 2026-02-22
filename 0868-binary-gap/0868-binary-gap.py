class Solution:
    def binaryGap(self, n: int) -> int:
        mx=0
        n=list(bin(n)[2:])
        f=n.index('1')
        for i in range(f+1,len(n)):
            if n[i]=='1':
                mx=max(mx,i-f)
                f=i
        return mx