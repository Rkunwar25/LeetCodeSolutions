class Solution(object):
    def kthDistinct(self, arr, k):
        d=0
        for i in range(len(arr)):
            if arr.count(arr[i])==1:
                d+=1
                if d==k:
                    return arr[i]
        return ""