class Solution(object):
    def maxFrequencyElements(self, nums):
        count = Counter(nums)
        max_freq = max(count.values())  # Find the maximum frequency
        return sum(frequency for frequency in count.values() if frequency == max_freq)