class Solution:
    def largestEven(self, s: str) -> str:
        # s=list(s)
        # print(s)
        # while s:
        #     ans="".join(s)
        #     num=int(ans)
        #     if num%2==0:
        #         return ans
        #     s.pop()
        # return ""
        for i in range(len(s)-1,-1,-1):
            if int(s[i])%2==0:
                return s[:i+1]
        return ""