class Solution(object):
    def validPalindrome(self, s):
        def isPalindrome(sub):
            return sub == sub[::-1]

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Try removing either the left or the right character
                return isPalindrome(s[left+1:right+1]) or isPalindrome(s[left:right])
            left += 1
            right -= 1
        return True