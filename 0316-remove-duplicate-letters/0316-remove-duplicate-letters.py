class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Store the last index of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            if char in seen:
                continue

            # Remove characters that are bigger than current and appear later again
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                removed = stack.pop()
                seen.remove(removed)
            
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
