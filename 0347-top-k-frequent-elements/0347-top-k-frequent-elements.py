class Solution(object):
    def topKFrequent(self, nums, k):
        c = Counter(nums).most_common(k)
        return [element for element, count in c]