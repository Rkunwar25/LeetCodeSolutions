# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        left = 1
        right = n
    
        while left <= right:
           mid = left + (right - left) // 2
           result = guess(mid)
        
           if result == 0:
              return mid  # Found the number
           elif result < 0:
              right = mid - 1  # The picked number is lower
           else:
              left = mid + 1   # The picked number is higher
            
        return -1  # In theory, this should never be reached