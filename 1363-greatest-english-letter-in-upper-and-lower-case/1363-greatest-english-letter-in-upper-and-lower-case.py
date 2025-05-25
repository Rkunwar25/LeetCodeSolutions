class Solution(object):
    def greatestLetter(self, s):
        greatest=0
        for i in range(ord('A'),ord('Z')+1):
            if (chr(i).lower() in s) and (chr(i) in s):
                greatest=i
        return chr(greatest) if greatest!=0 else ""