class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nset=set(nums)
        for i in nset:
            if nums.count(i)%2!=0:
                return False
        return True