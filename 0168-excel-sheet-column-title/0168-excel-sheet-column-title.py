class Solution(object):
    def convertToTitle(self, columnNumber):
        alph=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        title=""
        while columnNumber>0:
            columnNumber-=1
            title=alph[(columnNumber%26)]+title
            columnNumber//=26
        return title