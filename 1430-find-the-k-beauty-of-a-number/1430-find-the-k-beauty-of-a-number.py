class Solution(object):
    def divisorSubstrings(self, num, k):
        num_str = str(num)
        count = 0
    
        for i in range(len(num_str) - k + 1):
           substr = num_str[i:i + k]
           val = int(substr)
        
           if val != 0 and num % val == 0:
              count += 1
    
        return count