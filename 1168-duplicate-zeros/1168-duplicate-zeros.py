class Solution(object):
    def duplicateZeros(self, arr):
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                arr.pop()
                arr.insert(i + 1, 0)
                i += 2
            else:
                i += 1
