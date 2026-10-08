class Solution(object):
    def removeOuterParentheses(self, s):
        res = []
        level = 0

        for ch in s:
            if ch == '(':
                if level > 0:
                    res.append(ch)
                level += 1
            else:  # ch == ')'
                level -= 1
                if level > 0:
                    res.append(ch)

        return ''.join(res)
