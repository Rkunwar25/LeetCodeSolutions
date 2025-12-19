class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        n=list(str(n))        
        s=sum(map(int,n))
        n=[i for i in n if i!="0"]
        return int("".join(n))*s