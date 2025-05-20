class Solution(object):
    def sumOfNumberAndReverse(self, num):
        def reverse(x):
            return int(str(x)[::-1])
    
        for x in range(num + 1):
           if x + reverse(x) == num:
              return True
        return False
        