class Solution(object):
    def uniqueOccurrences(self, arr):
        count=Counter(arr)
        return len(count.values())==len(set(count.values()))
            