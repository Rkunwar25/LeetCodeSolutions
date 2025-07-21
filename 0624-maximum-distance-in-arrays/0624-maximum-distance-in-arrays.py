class Solution(object):
    def maxDistance(self, arrays):
        result = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        for i in range(1, len(arrays)):
            arr = arrays[i]
            result = max(result, abs(arr[-1] - min_val), abs(max_val - arr[0]))
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
        
        return result
