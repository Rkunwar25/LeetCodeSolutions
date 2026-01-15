class Solution(object):
    def partitionString(self, s):
        seen = set()
        segments = []
        curr = ""

        for ch in s:
            curr += ch
            if curr not in seen:
                segments.append(curr)
                seen.add(curr)
                curr = ""

        return segments
