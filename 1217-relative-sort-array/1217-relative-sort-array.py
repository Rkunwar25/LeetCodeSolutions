class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        count = Counter(arr1)
        result = []
        for num in arr2:
            result.extend([num] * count[num])
            del count[num] 
        leftovers = sorted(count.elements())
        result.extend(leftovers)

        return result