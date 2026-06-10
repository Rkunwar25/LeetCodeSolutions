class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        p=1
        for i in s:
            ans+=p*(27-(ord(i)-96))
            p+=1
        return ans