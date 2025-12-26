class Solution:
    def findMaxLength(self, nums):
        mp = {0: -1}   # sum -> index
        s = 0
        ans = 0

        for i, num in enumerate(nums):
            if num == 0:
                s -= 1
            else:
                s += 1

            if s in mp:
                ans = max(ans, i - mp[s])
            else:
                mp[s] = i

        return ans
