class Solution(object):
    def removeDigit(self, number, digit):
        l=[]
        for i in range(len(number)):
            if number[i]==digit:
                l.append(number[:i]+number[i+1:])
        return max(l)