class Solution(object):
    def convertDateToBinary(self, date):
        l=date.split("-")
        l1=[]
        for i in l:
           l1.append(bin(int(i))[2:])

        return '-'.join(l1)