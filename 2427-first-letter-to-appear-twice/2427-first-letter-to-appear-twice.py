class Solution(object):
    def repeatedCharacter(self, s):
        seen = set()
        for char in s:
          if char in seen:
             return char
          seen.add(char)