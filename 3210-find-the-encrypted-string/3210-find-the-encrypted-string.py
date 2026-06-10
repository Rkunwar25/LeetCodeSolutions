class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans=""
        n=len(s)
        for i in range(n):
            ans+=s[(i+k)%n]
        return ans