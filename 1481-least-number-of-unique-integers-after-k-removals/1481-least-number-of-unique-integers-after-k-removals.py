class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        result = sorted(arr, key=lambda x: (freq[x], x))
        result=result[k:]
        return len(set(result))