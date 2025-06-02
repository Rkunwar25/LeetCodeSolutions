class Solution(object):
    def percentageLetter(self, s, letter):
        if letter not in s:
            return 0
        c=list(s)
        val=c.count(letter)
        return int(val/float(len(s))*100)