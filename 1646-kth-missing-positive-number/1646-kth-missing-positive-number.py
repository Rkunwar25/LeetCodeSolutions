class Solution(object):
    def findKthPositive(self, arr, k):
        n=max(arr)+k
        l=[i for i in range(1,n+1)]
        arr=sorted(list(set(l)-set(arr)))
        # print(arr)
        return arr[k-1]