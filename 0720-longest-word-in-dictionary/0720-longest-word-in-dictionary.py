class Solution:
    def longestWord(self, words):
        words.sort()                 # lexicographical order
        words.sort(key=len)          # then by length

        built = set([""])            # base case
        ans = ""

        for word in words:
            if word[:-1] in built:
                built.add(word)
                if len(word) > len(ans):
                    ans = word

        return ans
