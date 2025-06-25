class Solution(object):
    def findClosestElements(self, arr, k, x):
        # Sort array by closeness to x, then by value
        sorted_arr = sorted(arr, key=lambda num: (abs(num - x), num))
        # Take the first k elements
        result = sorted(sorted_arr[:k])
        return result
