class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        indices=[]
        for i in range(len(nums)):
            if nums[i]==1:
                indices.append(i)
        print(indices)
        for i in range(1,len(indices)):
            if indices[i]-indices[i-1]<k+1:
                return False
        return True