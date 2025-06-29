class Solution(object):
    def maxScore(self, s):
        mx=float('-inf')
        for i in range(1,len(s)):
            mx=max(mx,s[:i].count('0')+s[i:].count('1'))
        return mx