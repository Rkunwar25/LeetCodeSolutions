class Solution(object):
    def findShortestSubArray(self, nums):
        first = {}
        last = {}
        count = {}

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1

        degree = max(count.values())
        min_len = float('inf')

        for num in count:
            if count[num] == degree:
                min_len = min(min_len, last[num] - first[num] + 1)

        return min_len
