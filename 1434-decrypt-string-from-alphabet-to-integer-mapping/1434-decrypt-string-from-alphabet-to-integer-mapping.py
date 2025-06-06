class Solution(object):
    def freqAlphabets(self, s):
        res = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                # Take 2 digits before '#'
                num = int(s[i-2:i])
                res.append(chr(ord('a') + num - 1))
                i -= 3
            else:
                num = int(s[i])
                res.append(chr(ord('a') + num - 1))
                i -= 1
        return ''.join(reversed(res))