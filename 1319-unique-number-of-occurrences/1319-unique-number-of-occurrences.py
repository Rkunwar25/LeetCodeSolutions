class Solution(object):
    def uniqueOccurrences(self, arr):
        count=Counter(arr)
        if len(count.values())==len(set(count.values())):
            return True
        return False         