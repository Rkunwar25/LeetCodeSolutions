class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1="qwertyuiop"
        line2="asdfghjkl"
        line3="zxcvbnm"
        l=[]
        for i in words:
            if all(ch in line1 for ch in i.lower()) or all(ch in line2 for ch in i.lower()) or all(ch in line3 for ch in i.lower()) :
                l.append(i)
        return l