class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s=sentence.split()
        m="maa"
        for i in range(len(s)):
            if s[i][0].lower() in 'aeiou':
                s[i]=s[i]+m
            else:
                s[i]=s[i][1:]+s[i][0]+m
            m+="a"
        return " ".join(s)