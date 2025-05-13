class Solution(object):
    def validMountainArray(self, arr):
        # mx=arr.index(max(arr))
        # if arr[mx]==arr[0] or arr[mx]==arr[len(arr)-1]:
        #     return False
        # elif sorted(arr[:mx])==arr[:mx] and sorted(arr[mx+1:],reverse=True)==arr[mx+1:]:
        #     return True
        # else:
        #     return False
        n = len(arr)
        if n < 3:
            return False
        
        # Climb up
        i = 0
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1
        
        # If peak is the first or last element, it's not a mountain
        if i == 0 or i == n - 1:
            return False
        
        # Climb down
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1
        
        # If we reach the end, it's a valid mountain array
        return i == n - 1