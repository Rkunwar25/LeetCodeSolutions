class Solution(object):
    def countHillValley(self, nums):
        # Remove consecutive duplicates
        compressed = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                compressed.append(nums[i])

        count = 0
        for i in range(1, len(compressed) - 1):
            if compressed[i] > compressed[i-1] and compressed[i] > compressed[i+1]:
                count += 1  # Hill
            elif compressed[i] < compressed[i-1] and compressed[i] < compressed[i+1]:
                count += 1  # Valley

        return count
