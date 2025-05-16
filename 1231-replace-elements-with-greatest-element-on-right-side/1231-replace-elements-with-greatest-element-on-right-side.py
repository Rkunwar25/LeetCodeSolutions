class Solution(object):
    def replaceElements(self, arr):
        max_right = -1
        
        # Iterate from the end to the beginning
        for i in range(len(arr) - 1, -1, -1):
            # Store the current element
            current = arr[i]
            
            # Replace current element with the max to its right
            arr[i] = max_right
            
            # Update max_right if current is larger
            max_right = max(max_right, current)
        
        return arr