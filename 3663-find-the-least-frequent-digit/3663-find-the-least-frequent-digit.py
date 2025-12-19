class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n=list(str(n))
        c=Counter(n)
        mn=float('inf')
        for i in c:
            if c[i]<mn:
                mn=c[i]
        minfreq=[]
        for i in c:
            if c[i]==mn:
                minfreq.append(i)
        return int(min(minfreq))