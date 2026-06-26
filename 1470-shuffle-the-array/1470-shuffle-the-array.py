class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1=nums[:n]
        l2=nums[n:]
        ans=[]
        for i in range(0,n):
            ans.append(l1[i])
            ans.append(l2[i])
        return ans