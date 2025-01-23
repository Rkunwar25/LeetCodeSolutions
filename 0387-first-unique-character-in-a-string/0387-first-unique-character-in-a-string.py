class Solution(object):
    def firstUniqChar(self, s):
        # for i in range(len(s)):
        #     if s.count(s[i])==1:
        #         return i
        # return -1
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Step 2: Find the first character with a count of 1
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        
        return -1