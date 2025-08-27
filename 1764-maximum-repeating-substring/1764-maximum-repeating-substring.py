class Solution(object):
    def maxRepeating(self, sequence, word):
        k = 0
        while word * (k + 1) in sequence:
            k += 1
        return k
