class Solution(object):
    def heightChecker(self, heights):
        h=sorted(heights)
        c=0
        for i in range(len(h)):
            if h[i]!=heights[i]:
                c+=1
        return c