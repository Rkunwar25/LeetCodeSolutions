class Solution(object):
    def binaryGap(self, n):
        n = list(bin(n)[2:])
        mx = 0
        i = 0

        while i < len(n):
             if n[i] == '1':
                 l = n[i+1:]
                 if '1' in l:
                     dist = l.index('1') + 1
                     mx = max(mx, dist)
                     i += dist
                 else:
                     break
             else:
                 i += 1
        return mx