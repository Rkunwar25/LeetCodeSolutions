class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = reduce(lambda a, b: a & b, map(Counter, nums))
        return sorted(list(common.elements()))