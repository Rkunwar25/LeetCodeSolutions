class Solution:
    def largestEven(self, s: str) -> str:
        s=list(s)
        print(s)
        while s:
            ans="".join(s)
            num=int(ans)
            if num%2==0:
                return ans
            s.pop()
        return ""