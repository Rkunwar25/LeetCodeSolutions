class Solution(object):
    def findRelativeRanks(self, score):
        l = sorted(score, reverse=True)
        d = {}
        for i in range(len(l)):
            if i == 0:
                d[l[i]] = "Gold Medal"
            elif i == 1:
                d[l[i]] = "Silver Medal"
            elif i == 2:
                d[l[i]] = "Bronze Medal"
            else:
                d[l[i]] = str(i + 1)
        return [d[s] for s in score]