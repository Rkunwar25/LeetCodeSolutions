class Solution(object):
    def rotateString(self, s, goal):
        n = len(s)
        left_shifts = [s[i:] + s[:i] for i in range(1, n)]
        left_shifts.append(s)
        if goal in left_shifts:
            return True
        else:
            return False