class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        c1=Counter(magazine)
        c2=Counter(ransomNote)
        
        for i in ransomNote:
            if (i not in magazine) or c2[i]>c1[i]:
                return False
        return True