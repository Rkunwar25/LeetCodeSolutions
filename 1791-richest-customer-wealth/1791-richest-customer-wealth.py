class Solution(object):
    def maximumWealth(self, accounts):
        l=[]
        for i in range(len(accounts)):
            l.append(sum(accounts[i]))
        return max(l)