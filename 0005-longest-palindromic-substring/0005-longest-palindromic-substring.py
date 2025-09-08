class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        start, end = 0, 0
        
        def expandAroundCenter(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # length of palindrome
        
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i)      # odd length
            len2 = expandAroundCenter(i, i + 1)  # even length
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def isPalindrome(sub):
#             return sub == sub[::-1]  # check if string equals its reverse
        
#         longest = ""
#         for i in range(len(s)):
#             for j in range(i+1, len(s)+1):
#                 sub = s[i:j]
#                 if isPalindrome(sub) and len(sub) > len(longest):
#                     longest = sub
#         return longest
