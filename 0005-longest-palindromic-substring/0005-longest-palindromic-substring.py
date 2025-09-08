class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(sub):
            return sub == sub[::-1]  # check if string equals its reverse
        
        longest = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if isPalindrome(sub) and len(sub) > len(longest):
                    longest = sub
        return longest