class Solution(object):
    def findLucky(self, arr):
        c=Counter(arr)
        max_lucky=-1
        for i,j in c.items():
            if i == j:
                max_lucky = max(max_lucky, i)
        return max_lucky