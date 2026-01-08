class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        count = 0
        for x in nums:
            if x - diff in s and x + diff in s:
                count += 1
        return count
