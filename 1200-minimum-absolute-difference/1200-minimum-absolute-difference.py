class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mn_d=float('inf')
        arr=sorted(arr)
        ans=[]
        for i in range(1,len(arr)):
           mn_d=min(mn_d,arr[i]-arr[i-1])
        for i in range(1,len(arr)):
           if arr[i]-arr[i-1]==mn_d:
            ans.append([arr[i-1],arr[i]])
        return ans