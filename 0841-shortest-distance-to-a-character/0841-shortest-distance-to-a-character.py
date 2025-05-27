class Solution(object):
    def shortestToChar(self, s, c):
        l = []
        for i in range(len(s)):
            min_dist = float('inf')  # Start with a large value
            for j in range(len(s)):
                if s[j] == c:
                    dist = abs(i - j)
                    if dist < min_dist:
                        min_dist = dist
            l.append(min_dist)
        
        return l