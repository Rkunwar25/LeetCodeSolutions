from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)

        # Step 1: count products of all pairs
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        # Step 2: count valid tuples
        result = 0
        for k in product_count.values():
            if k > 1:
                result += (k * (k - 1) // 2) * 8

        return result
