class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d=len(arr)/4
        for i in arr:
            if arr.count(i)>d:
                return i