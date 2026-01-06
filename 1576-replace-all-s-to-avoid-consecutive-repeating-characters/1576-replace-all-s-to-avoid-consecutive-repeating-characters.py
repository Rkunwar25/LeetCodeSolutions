class Solution(object):
    def modifyString(self, s):
        letters = list('abcdefghijklmnopqrstuvwxyz')
        s = list(s)

        for i in range(len(s)):
            if s[i] == '?':
                for ch in letters:
                    if (i > 0 and s[i-1] == ch):
                        continue
                    if (i < len(s)-1 and s[i+1] == ch):
                        continue
                    s[i] = ch
                    break

        return "".join(s)
