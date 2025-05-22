class Solution(object):
    def trimMean(self, arr):
        n=len(arr)
        s=n*0.05
        arr.sort()
        for i in range(int(s)):
            arr.pop()
            arr.pop(0)
            n-=2
        return float(sum(arr))/n
