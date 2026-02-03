class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0

        # 1️⃣ strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False

        # 2️⃣ strictly decreasing
        j = i
        while j + 1 < n and nums[j] > nums[j + 1]:
            j += 1
        if j == i:
            return False

        # 3️⃣ strictly increasing
        k = j
        while k + 1 < n and nums[k] < nums[k + 1]:
            k += 1

        # 🔥 crucial fix: third segment must have at least one step
        if k == j:
            return False

        return k == n - 1
