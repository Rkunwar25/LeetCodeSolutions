class Solution(object):
    def checkRecord(self, s):
            return s.count('A') < 2 and 'LLL' not in s
