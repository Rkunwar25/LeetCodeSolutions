class Solution(object):
    def mostFrequentEven(self, nums):
        even_nums = [num for num in nums if num % 2 == 0]
        if not even_nums:
            return -1
        freq = Counter(even_nums)
        return min(freq.keys(), key=lambda x: (-freq[x], x))