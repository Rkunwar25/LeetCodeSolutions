class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            result = result * 26 + value
        return result