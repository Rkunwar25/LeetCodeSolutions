class Solution:
    def numSteps(self, s: str) -> int:
        count=0
        n=int(s,2)
        while n!=1:
            if n%2==0:
                n//=2
            else:
                n+=1
            count+=1
        return count