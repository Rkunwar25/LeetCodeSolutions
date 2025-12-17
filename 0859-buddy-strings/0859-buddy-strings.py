class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # Length must be same
        if len(s) != len(goal):
            return False
        
        # Case 1: Strings are already equal
        # We need at least one duplicate character to allow a valid swap
        if s == goal:
            return len(set(s)) < len(s)
        
        # Case 2: Strings are different
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False
        
        # Exactly two differences and swap should fix it
        return (
            len(diff) == 2 and
            s[diff[0]] == goal[diff[1]] and
            s[diff[1]] == goal[diff[0]]
        )
